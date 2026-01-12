# Enhancement Roadmap - Phases 6-9

**Date:** 2026-01-10 (Updated: 2026-01-11)
**Status:** 🚧 IN PROGRESS
**Previous Phases:** 1-5 Complete (V2 Implementation)
**Current Phase:** 6 (Bug Fixes & Polish)

---

## Executive Summary

V2 is complete and deployed. This roadmap covers the next phase of development focusing on:
- **Phase 6:** Bug fixes from code review
- **Phase 7:** Feature completion (auto-tuning, rate limiting)
- **Phase 8:** Testing and documentation
- **Phase 9:** Advanced features (future)

**Timeline:** 6-8 weeks
**Current Focus:** Address critical bugs, complete in-progress features

---

## 📊 Current State Assessment

### What's Complete ✅
- V2 unified text architecture (not JSON - structured text format)
- Beautiful TUI with ASCII art
- Pip-installable package
- Configuration management
- Enhanced test command
- Auto-tuning system (70% complete)

### What Needs Work 🚧
- **2 Critical bugs** from code review
- **6 Medium issues** affecting quality
- **Auto-tuning** needs completion (testing phase)
- **Rate limiting** documented but not implemented
- **Logging system** missing
- **Test coverage** at ~60% (need >90%)

---

## Phase 6: Bug Fixes & Polish (Week 1)

**Goal:** Address all critical and medium priority issues from code review

**Status:** 🔴 NOT STARTED
**Priority:** HIGHEST
**Duration:** 1 week
**Dependencies:** None (can start immediately)

---

### 6.1: Critical Bug Fixes (Days 1-2)

#### Task 6.1.1: Fix Schema-Parser Mismatch ⚠️ HIGH PRIORITY

**Issue:** LLM generates DEPENDENCIES section but parser doesn't extract it

**Location:**
- `ralf_notes/core/schema.py` (schema definition)
- `ralf_notes/core/text_parser.py` (parser implementation)

**Fix:**
```python
# In text_parser.py - Add to parse() method:

def parse(self, raw_text: str) -> Dict[str, Any]:
    sections = self._split_into_sections(raw_text)

    parsed_data = {
        "filename": self._parse_filename(sections.get("FILENAME", "")),
        "summary": self._parse_summary(sections.get("SUMMARY", "")),
        "tags": self._parse_tags(sections.get("TAGS", "")),
        "type": self._parse_type(sections.get("TYPE", "")),
        "key_functions": self._parse_key_functions(sections.get("KEY_FUNCTIONS", "")),
        "details": self._parse_details(sections.get("DETAILS", "")),
        "dependencies": self._parse_dependencies(sections.get("DEPENDENCIES", "")),  # ADD
        "usage": self._parse_usage(sections.get("USAGE", "")),
        "related": self._parse_related(sections.get("RELATED", "")),
        "callouts": self._parse_callouts(sections.get("CALLOUTS", "")),
    }
    return parsed_data

def _parse_filename(self, content: str) -> str:
    """Extract filename."""
    return content.strip()

def _parse_dependencies(self, content: str) -> List[str]:
    """Parse comma-separated dependencies."""
    if not content or content.lower() == 'none':
        return []
    return [dep.strip() for dep in content.split(',') if dep.strip()]
```

**Testing:**
- Generate documentation for file with dependencies
- Verify dependencies appear in output
- Check formatted markdown has Dependencies section

**Files to Update:**
- `ralf_notes/core/text_parser.py`

**Deliverable:** Dependencies section properly parsed and formatted

---

#### Task 6.1.2: Fix Config Propagation ⚠️ HIGH PRIORITY

**Issue:** `max_content_length` and `max_chunk_summary_length` not passed from config to generator

**Location:** `ralf_notes/cli.py:95-108` (build_pipeline function)

**Current Code:**
```python
def build_pipeline(config_manager: ConfigManager) -> DocumentPipeline:
    client = Client(host=config_manager.get("ollama_host"))
    gen_config = StructuredTextGeneratorConfig(
        model_name=config_manager.get("model_name"),
        num_ctx=config_manager.get("num_ctx"),
        temperature=config_manager.get("temperature"),
        chunk_size=config_manager.get("chunk_size"),
        ollama_host=config_manager.get("ollama_host")
        # MISSING: max_content_length
        # MISSING: max_chunk_summary_length
    )
```

**Fix:**
```python
def build_pipeline(config_manager: ConfigManager) -> DocumentPipeline:
    client = Client(host=config_manager.get("ollama_host"))
    gen_config = StructuredTextGeneratorConfig(
        model_name=config_manager.get("model_name"),
        num_ctx=config_manager.get("num_ctx"),
        temperature=config_manager.get("temperature"),
        chunk_size=config_manager.get("chunk_size"),
        max_content_length=config_manager.get("max_content_length"),  # ADD
        max_chunk_summary_length=config_manager.get("max_chunk_summary_length"),  # ADD
        ollama_host=config_manager.get("ollama_host")
    )
    # ... rest of code
```

**Testing:**
- Set custom values in config
- Verify they're used in generation
- Test with very large files

**Files to Update:**
- `ralf_notes/cli.py:95-108`

**Deliverable:** All config values properly propagated

---

#### Task 6.1.3: Fix Metadata Inconsistency

**Issue:** Success path uses 'data' key, error paths use 'parsed_data' key

**Location:** `ralf_notes/core/document_pipeline.py:99, 119`

**Fix:**
```python
# Change both error handlers to use 'data' consistently:
metadata = {
    'cached': False,
    'valid': False,
    'errors': [error_message],
    'data': {}  # Changed from 'parsed_data'
}
```

**Testing:**
- Test successful generation
- Test error cases
- Verify metadata structure consistent

**Files to Update:**
- `ralf_notes/core/document_pipeline.py`

**Deliverable:** Consistent metadata structure

---

### 6.2: Medium Priority Fixes (Days 3-5)

#### Task 6.2.1: Resolve Filename Handling

**Issue:** Filename in schema but overridden from file system anyway

**Decision:** Remove FILENAME from schema (simpler, trust file system)

**Files to Update:**
- `ralf_notes/core/schema.py` - Remove FILENAME section from prompt
- `ralf_notes/core/text_parser.py` - Always inject filename from parameter
- Update parse_or_fallback to not extract FILENAME

**Testing:**
- Verify filename still appears in output

---

#### Task 6.2.3: Fix Timing Display Bug 🔴 NEW

**Issue:** Time and Speed showing 0.0 in summary results

**Location:** `ralf_notes/cli.py` - All three stage functions

**Problem:**
- `_generate_raw_logic()` (lines 337-338) - hardcoded duration/speed to 0
- `_format_initial_logic()` (lines 428-434) - missing duration/speed fields
- `_finalize_logic()` - similar issue

**Fix Required:**

```python
def _stage_function(...):
    import time
    start_time = time.time()  # ADD at function start

    # ... existing code ...
    processed_count = 0
    failed_count = 0
    skipped_count = 0

    # ... processing loop ...

    duration = time.time() - start_time  # ADD before results dict

    results = {
        'total': processed_count + failed_count + skipped_count,
        'success': processed_count,
        'failed': failed_count,
        'skipped': skipped_count,
        'dry_run': dry_run,
        'duration': duration,  # ADD
        'files_per_second': processed_count / duration if duration > 0 else 0  # ADD
    }
```

**Files to Update:**
- `ralf_notes/cli.py:_generate_raw_logic()` - Add timing
- `ralf_notes/cli.py:_format_initial_logic()` - Add timing
- `ralf_notes/cli.py:_finalize_logic()` - Add timing

**Testing:**
- Run `ralf-notes generate` and verify Time/Speed shown
- Verify accurate values (not 0.0)
- Test with large batches

**Deliverable:** Accurate timing information in all commands

**Reference:** See `feedback/12-display-bugs-jan-2026.md` for full analysis

**Estimate:** 30 minutes
- Verify LLM doesn't generate FILENAME section
- Check generated markdown

**Deliverable:** Cleaner schema, fewer wasted tokens

---

#### Task 6.2.2: Clean Up Formatter Dead Code

**Issue:** NoteFormatter has methods for sections parser never extracts

**Decision:** Remove unused formatters (simpler than adding parsers)

**Sections to Remove:**
- `_format_code_summary()` (unless we want to add parser for this)
- `_format_security_risks()` (unless we want to add parser for this)
- `_format_performance_notes()` (unless we want to add parser for this)
- `_format_dependency_graph()` (unless we want to add parser for this)

**OR:** Add parsers for these sections to schema

**Recommendation:** Remove unused formatters (KISS principle)

**Files to Update:**
- `ralf_notes/core/note_formatter.py` - Remove unused methods
- Update format() method to not call them

**Testing:**
- Verify output still correct
- Check no dead code warnings

**Deliverable:** Clean formatter with only used methods

---

#### Task 6.2.3: Implement Basic Rate Limiting

**Issue:** Rate limiting documented in `08-rate-limit-options.md` but not implemented

**Priority Items to Implement:**
1. Request delay (time.sleep between files)
2. Timeout limits (max time per request)
3. Retry with backoff (exponential backoff on errors)

**Implementation:**

```python
# In file_processor.py:

def process_paths(self, ...):
    # Get rate limit config
    request_delay = self.config_manager.get('request_delay_seconds', 0)
    timeout = self.config_manager.get('request_timeout_seconds', 300)

    for i, file_path in enumerate(files, 1):
        # Process with timeout
        try:
            with timeout_context(timeout):
                markdown, metadata = self.pipeline.generate_document(file_path)
        except TimeoutError:
            # Handle timeout

        # Apply delay between requests
        if request_delay > 0 and i < len(files):
            time.sleep(request_delay)

# In structured_text_generator.py - add retry logic:

def generate_with_retry(self, context: GenerationContext, max_retries=3) -> str:
    backoff = 1
    for attempt in range(max_retries):
        try:
            return self.generate(context)
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff)
            backoff *= 2  # Exponential backoff
```

**Config Updates:**
```python
# In config_manager.py DEFAULT_CONFIG:
"request_delay_seconds": 0,  # 0 = no delay
"request_timeout_seconds": 300,  # 5 minutes
"retry_attempts": 3,
"initial_backoff_seconds": 1,
"backoff_multiplier": 2
```

**CLI Updates:**
```python
# Add options to generate command:
@app.command()
def generate(
    delay: Optional[float] = typer.Option(None, "--delay", help="Delay between files (seconds)"),
    timeout: Optional[int] = typer.Option(None, "--timeout", help="Timeout per file (seconds)"),
    retries: Optional[int] = typer.Option(None, "--retries", help="Retry attempts"),
):
    if delay is not None:
        config_manager.set("request_delay_seconds", delay)
    if timeout is not None:
        config_manager.set("request_timeout_seconds", timeout)
    if retries is not None:
        config_manager.set("retry_attempts", retries)
```

**Files to Update:**
- `ralf_notes/core/file_processor.py`
- `ralf_notes/core/structured_text_generator.py`
- `ralf_notes/config_manager.py`
- `ralf_notes/cli.py`

**Testing:**
- Test with various delay values
- Test timeout on slow requests
- Test retry on failures

**Deliverable:** Working rate limiting with CLI options

---

#### Task 6.2.4: Add Comprehensive Logging

**Issue:** No logging system - debugging production issues is difficult

**Implementation:**

```python
# Create ralf_notes/utils/logger.py:

import logging
from pathlib import Path

def setup_logging(log_level: str = "INFO", log_file: Optional[Path] = None):
    """Set up logging for RALF Notes."""
    if log_file is None:
        log_file = Path.home() / ".ralf-notes" / "ralf-notes.log"

    log_file.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

# In each module:
import logging
logger = logging.getLogger(__name__)

# Usage:
logger.info("Processing file: %s", file_path)
logger.warning("Chunk summarization failed: %s", error)
logger.error("Pipeline failed: %s", error, exc_info=True)
```

**Config Updates:**
```python
# In config_manager.py DEFAULT_CONFIG:
"log_level": "INFO",  # DEBUG, INFO, WARNING, ERROR
"log_file": None,  # None = default location
```

**Files to Update:**
- Create `ralf_notes/utils/logger.py`
- Add logging to all core modules
- Update CLI to initialize logging
- Add to config

**Testing:**
- Verify logs written to file
- Check log rotation
- Test different log levels

**Deliverable:** Comprehensive logging throughout application

---

### 6.3: Polish & Validation (Day 6-7)

#### Task 6.3.1: Input Validation

**Add validation to CLI commands:**
- Validate file paths exist
- Validate numeric inputs (temperature 0-2, num_ctx > 0)
- Validate model names
- Validate directories are writable

**Files to Update:**
- `ralf_notes/cli.py` - Add validation to all commands

---

#### Task 6.3.2: Create Test Suite

**Tests to Add:**
- Schema-parser alignment test
- Config propagation test
- Error handling test
- Rate limiting test
- Metadata consistency test

**Files to Create:**
- `tests/test_parser_schema_alignment.py`
- `tests/test_config_propagation.py`
- `tests/test_error_handling.py`

---

#### Task 6.3.3: Update Documentation

**Documents to Update:**
- Update README with new features
- Document rate limiting options
- Add troubleshooting guide
- Update CLI help text

---

## Phase 7: Feature Completion (Week 2-3)

**Goal:** Complete auto-tuning system and polish features

**Status:** 🟡 PLANNED
**Priority:** HIGH
**Duration:** 2 weeks
**Dependencies:** Phase 6 complete

---

### 7.1: Complete Auto-Tuning System

#### Task 7.1.1: Finish ModelBenchmarker

**Remaining Work:**
- [ ] Context size testing implementation
- [ ] Chunk size testing implementation
- [ ] Quality scoring algorithm
- [ ] Validation of results

**Files to Update:**
- `ralf_notes/tuning/model_benchmarker.py`

---

#### Task 7.1.2: Finish ThroughputBenchmarker

**Remaining Work:**
- [ ] Sequential vs parallel comparison
- [ ] Real-world scenario testing
- [ ] Memory usage tracking
- [ ] CPU utilization monitoring

**Files to Update:**
- `ralf_notes/tuning/throughput_benchmarker.py`

---

#### Task 7.1.3: Testing & Validation

**Tasks:**
- Test on different systems (low-end, high-end)
- Validate recommendations are sensible
- Error handling for benchmark failures
- Add resume capability for long benchmarks
- Cache benchmark results

---

### 7.2: Polish Features

#### Task 7.2.1: Progress Callbacks

**Add progress feedback for:**
- Recursive summarization
- Large batch processing
- Benchmark operations

---

#### Task 7.2.2: Better Error Messages

**Improve error messages:**
- User-friendly descriptions
- Suggested fixes
- Links to documentation

---

## Phase 8: Testing & Documentation (Week 4)

**Goal:** Achieve >90% test coverage and complete documentation

**Status:** 🟡 PLANNED
**Priority:** MEDIUM
**Duration:** 1 week
**Dependencies:** Phases 6-7 complete

---

### 8.1: Comprehensive Testing

**Test Categories:**
1. **Unit Tests** - All core components
2. **Integration Tests** - Full pipelines
3. **Performance Tests** - Benchmark validation
4. **Error Tests** - Edge cases and failures

**Target:** >90% code coverage

---

### 8.2: Documentation

**Documents to Create:**
1. **User Guide** - Complete usage guide
2. **Troubleshooting** - Common issues and fixes
3. **API Reference** - For developers
4. **Examples** - Real-world usage examples
5. **Tutorial** - Step-by-step getting started

---

## Phase 9: Advanced Features (Future)

**Goal:** Optional enhancements based on user needs

**Status:** 🔵 FUTURE
**Priority:** LOW
**Duration:** TBD
**Dependencies:** User feedback

---

### Potential Features

#### 9.1: Watch Mode
- Auto-regenerate on file changes
- File system monitoring
- Incremental updates

#### 9.2: Parallel Processing
- Process multiple files simultaneously
- Thread pool or multiprocessing
- Configurable workers

#### 9.3: Smart Model Selection
- Different models for different file types
- Size-based model selection
- Quality-based routing

#### 9.4: Web Interface (Optional)
- Browser-based UI
- REST API
- Dashboard for monitoring

#### 9.5: Plugin System
- Custom generators
- Custom formatters
- Extension points

#### 9.6: Integration Features
- Git hooks integration
- CI/CD integration
- IDE plugins

#### 9.7: Tag Refinement System 🆕

**Status:** Designed, ready for implementation

**Purpose:** Analyze and refine tags across all generated documentation

**Commands:**
```bash
# Analyze tags and generate refinement guide
ralf-notes tags analyze ~/to_obsidian --output guide.json

# Apply refinements
ralf-notes tags apply ~/to_obsidian --guide guide.json --dry-run

# Show tag statistics
ralf-notes tags stats ~/to_obsidian
```

**Components:**
1. **TagCollector** - Extract all tags from frontmatter
2. **TagAnalyzer** - Find patterns and grouping opportunities
3. **TagRefinementLLM** - LLM-powered suggestions
4. **RefinementGuideBuilder** - Create JSON guide
5. **TagReplacer** - Apply refinements to files

**Benefits:**
- Cleaner, more consistent tags
- Reduced redundancy
- AI-powered suggestions
- Better Obsidian navigation

**Design Document:** [11-tag-refinement-system.md](11-tag-refinement-system.md)

**Implementation Estimate:** 3 weeks
- Week 1: Core analysis boxes
- Week 2: Application system
- Week 3: Polish and testing

**Priority:** Medium (good for Phase 9)

---

## Success Criteria

### Phase 6: Bug Fixes
- [ ] All critical bugs resolved
- [ ] All medium issues addressed
- [ ] Rate limiting implemented
- [ ] Logging system working
- [ ] Code review score: 9/10+

### Phase 7: Feature Completion
- [ ] Auto-tuning fully functional
- [ ] `ralf-notes fine-tune` command works on all systems
- [ ] Progress feedback implemented
- [ ] Error messages improved

### Phase 8: Testing & Documentation
- [ ] >90% test coverage achieved
- [ ] All integration tests passing
- [ ] Complete user guide published
- [ ] Troubleshooting guide complete

### Phase 9: Advanced Features
- [ ] At least 2 advanced features implemented
- [ ] User feedback incorporated
- [ ] Stable and well-tested

---

## Risk Management

### Technical Risks

**Risk:** Breaking changes during bug fixes
**Mitigation:** Comprehensive test suite, careful refactoring

**Risk:** Auto-tuning gives bad recommendations
**Mitigation:** Validation tests, user override options

**Risk:** Performance degradation with new features
**Mitigation:** Benchmark before/after, optimization

### Process Risks

**Risk:** Feature creep
**Mitigation:** Stick to roadmap, prioritize ruthlessly

**Risk:** Test coverage slips
**Mitigation:** Automated coverage checks, CI/CD

---

## Timeline Summary

| Phase | Focus | Duration | Status |
|-------|-------|----------|--------|
| **6** | Bug Fixes & Polish | 1 week | 🔴 Not Started |
| **7** | Feature Completion | 2 weeks | 🟡 Planned |
| **8** | Testing & Documentation | 1 week | 🟡 Planned |
| **9** | Advanced Features | TBD | 🔵 Future |

**Total (Phases 6-8):** 4 weeks
**With Advanced Features:** 6-8 weeks

---

## Progress Tracking

### Phase 6 Progress: 0/13 Complete
- [ ] 6.1.1: Fix schema-parser mismatch
- [ ] 6.1.2: Fix config propagation
- [ ] 6.1.3: Fix metadata inconsistency
- [ ] 6.2.1: Resolve filename handling
- [ ] 6.2.2: Clean up formatter dead code
- [ ] 6.2.3: Implement rate limiting
- [ ] 6.2.4: Add logging system
- [ ] 6.3.1: Input validation
- [ ] 6.3.2: Create test suite
- [ ] 6.3.3: Update documentation

### Phase 7 Progress: 0/6 Complete
- [ ] 7.1.1: Finish ModelBenchmarker
- [ ] 7.1.2: Finish ThroughputBenchmarker
- [ ] 7.1.3: Testing & validation
- [ ] 7.2.1: Progress callbacks
- [ ] 7.2.2: Better error messages

### Phase 8 Progress: 0/2 Complete
- [ ] 8.1: Comprehensive testing
- [ ] 8.2: Documentation

---

## Next Actions

### This Week (Phase 6 Start)
1. ✅ Complete roadmap alignment (this document)
2. 🔴 Start critical bug fixes
3. 🔴 Fix schema-parser mismatch
4. 🔴 Fix config propagation

### Next Week
5. Continue medium priority fixes
6. Implement rate limiting
7. Add logging system
8. Create initial tests

### Following Weeks
- Complete auto-tuning system
- Add comprehensive testing
- Write documentation
- Release stable version

---

## Conclusion

**Current Focus:** Phase 6 - Bug Fixes & Polish

**Priority:** Address 2 critical bugs and 6 medium issues identified in code review

**Next Milestone:** Complete Phase 6 with all bugs resolved and basic rate limiting implemented

**Long-term Goal:** Stable, well-tested, fully-featured documentation generator

The project has an excellent foundation (V2 complete). The focus now is on polish, completeness, and quality. Phases 6-8 will bring the project to production excellence.

---

**Document Version:** 1.0
**Date:** 2026-01-10
**Status:** Active Roadmap
**Next Update:** After Phase 6 completion
