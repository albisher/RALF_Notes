# Enhancement 1: Parallel Section Generation

## Priority: ⭐⭐⭐⭐⭐ HIGHEST IMPACT

## Problem
Currently, RALF Notes makes **8 sequential Ollama calls per file**:
- SUMMARY_PROMPT
- DETAILS_PROMPT
- KEY_FUNCTIONS_PROMPT
- USAGE_PROMPT
- RELATED_PROMPT
- TAGS_PROMPT
- TYPE_PROMPT
- DEPENDENCY_GRAPH_PROMPT
- SECURITY_RISKS_PROMPT

For 100 files, this means 900+ sequential LLM calls, which can take hours.

## Current Code Location
`main.py:459-601` - `generate_obsidian_doc()` function

## Solution
Use Python's `concurrent.futures` to run independent sections in parallel. Ollama's HTTP API supports concurrent requests naturally.

## Implementation

### Step 1: Add imports at top of main.py
```python
import concurrent.futures
import threading
```

### Step 2: Create thread-safe section generator
```python
def generate_section_safe(section_type, prompt, system_prompt, options):
    """Thread-safe section generation for parallel execution"""
    try:
        response = safe_generate(
            client,
            system=system_prompt,
            prompt=prompt,
            options=options,
            prompt_type=section_type
        )
        return section_type, response
    except Exception as e:
        logger.error(f"Failed to generate {section_type}: {e}")
        return section_type, None
```

### Step 3: Replace generate_obsidian_doc() with parallel version
```python
def generate_obsidian_doc(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_content = f.read()
    except Exception as e:
        logger.error(f"Error reading {file_path}: {e}")
        return None

    file_size = len(raw_content)
    file_name = os.path.basename(file_path)
    file_name_without_ext, file_ext = os.path.splitext(file_name)

    processed_content = recursive_summarize(raw_content)

    options = {
        "num_ctx": min(estimate_tokens(processed_content) + 2048, MAX_CTX),
        "temperature": 0.2,
        "keep_alive": "30m"
    }

    system_prompt = f"{RALF_ANALYST_PERSONA}\n\n{TASK_ANALYZE_AND_GENERATE}\n\n**Output Requirements:**\n{OUTPUT_FRONTMATTER}\n{OUTPUT_DOCUMENT_STRUCTURE}\n{CONTENT_INSTRUCTIONS}\n{CRUCIAL_RULES}\n\nBegin."

    # Calculate dynamic parameters
    summary_length = get_summary_length(file_size)
    num_tags = get_dynamic_count(file_size, 5, 20, 10000)
    num_links = get_dynamic_count(file_size, 2, 30, 10000)

    # Prepare all prompts
    prompts_to_run = {
        'SUMMARY': (SUMMARY_PROMPT.format(processed_content=processed_content, summary_length=summary_length), system_prompt, options),
        'DETAILS': (DETAILS_PROMPT.format(processed_content=processed_content), system_prompt, options),
        'KEY_FUNCTIONS': (KEY_FUNCTIONS_PROMPT.format(processed_content=processed_content), system_prompt, options),
        'USAGE': (USAGE_PROMPT.format(processed_content=processed_content), system_prompt, options),
        'RELATED': (RELATED_PROMPT.format(processed_content=processed_content, num_links=num_links), system_prompt, options),
        'TAGS': (TAGS_PROMPT.format(processed_content=processed_content, num_tags=num_tags), system_prompt, options),
        'TYPE': (TYPE_PROMPT.format(processed_content=processed_content), system_prompt, options),
        'DEPENDENCY_GRAPH': (DEPENDENCY_GRAPH_PROMPT.format(processed_content=processed_content), system_prompt, options),
        'SECURITY_RISKS': (SECURITY_RISKS_PROMPT.format(processed_content=processed_content), system_prompt, options),
    }

    # Run all sections in parallel (max 4 concurrent to avoid overwhelming Ollama)
    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        future_to_section = {
            executor.submit(generate_section_safe, section, *args): section
            for section, args in prompts_to_run.items()
        }

        for future in concurrent.futures.as_completed(future_to_section):
            section = future_to_section[future]
            section_type, response = future.result()
            if response:
                results[section_type] = response
            else:
                logger.error(f"Section {section_type} failed, using placeholder")
                results[section_type] = "Not applicable"

    # Validate and clean results (sequential, but fast)
    summary = validate_and_regenerate(
        results['SUMMARY'],
        is_summary_valid,
        SUMMARY_PROMPT,
        system_prompt,
        options,
        "SUMMARY_PROMPT",
        processed_content,
        {'summary_length': summary_length}
    )
    summary = clean_summary(summary)

    details = validate_and_regenerate(
        results['DETAILS'],
        has_no_questions,
        DETAILS_PROMPT,
        system_prompt,
        options,
        "DETAILS_PROMPT",
        processed_content
    )
    details = clean_details(details)

    key_functions = validate_and_regenerate(
        results['KEY_FUNCTIONS'],
        has_no_questions,
        KEY_FUNCTIONS_PROMPT,
        system_prompt,
        options,
        "KEY_FUNCTIONS_PROMPT",
        processed_content
    )
    key_functions = clean_not_applicable(key_functions)

    usage = validate_and_regenerate(
        results['USAGE'],
        has_no_questions,
        USAGE_PROMPT,
        system_prompt,
        options,
        "USAGE_PROMPT",
        processed_content
    )
    usage = clean_not_applicable(usage)

    related = validate_and_regenerate(
        results['RELATED'],
        has_no_questions,
        RELATED_PROMPT,
        system_prompt,
        options,
        "RELATED_PROMPT",
        processed_content,
        {'num_links': num_links}
    )
    related = clean_related(related)

    tags = validate_and_regenerate(
        results['TAGS'],
        lambda t: is_tags_valid(t, num_tags),
        TAGS_PROMPT,
        system_prompt,
        options,
        "TAGS_PROMPT",
        processed_content,
        {'num_tags': num_tags}
    )
    tags = clean_tags(tags)

    doc_type = results['TYPE']
    doc_type = clean_doc_type(doc_type)

    dependency_graph = validate_and_regenerate(
        results['DEPENDENCY_GRAPH'],
        has_no_questions,
        DEPENDENCY_GRAPH_PROMPT,
        system_prompt,
        options,
        "DEPENDENCY_GRAPH_PROMPT",
        processed_content
    )
    dependency_graph = clean_mermaid(dependency_graph)

    security_risks = validate_and_regenerate(
        results['SECURITY_RISKS'],
        has_no_questions,
        SECURITY_RISKS_PROMPT,
        system_prompt,
        options,
        "SECURITY_RISKS_PROMPT",
        processed_content
    )
    security_risks = clean_not_applicable(security_risks)

    # Rest of document assembly remains the same (lines 533-601)
    # ... [keep existing assembly code]
```

## Expected Impact
- **Speed improvement:** 5-7x faster per file
- **Resource usage:** Better CPU utilization (Ollama can handle 4-8 concurrent requests)
- **User experience:** Significantly faster overall processing

## Configuration Options

Add to `config.py`:
```python
# Parallel processing configuration
MAX_CONCURRENT_SECTIONS = 4  # Adjust based on your hardware (M4 can handle 6-8)
```

Update the executor:
```python
with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT_SECTIONS) as executor:
```

## Testing
1. Process a single small file and verify all sections generate correctly
2. Process 10 files and compare timing vs. sequential version
3. Monitor Ollama logs for any errors or throttling

## Rollback Plan
If issues arise, the original sequential code is preserved in git. Simply revert the `generate_obsidian_doc()` function.

## Notes
- Ollama's HTTP API is stateless and thread-safe
- The validation/cleaning steps remain sequential (they're fast)
- Document assembly is sequential (it's fast and deterministic)
- Only the LLM generation is parallelized (the bottleneck)
