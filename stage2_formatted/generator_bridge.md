**Tags:** #dynamic-loading, #python-generator, #module-importer, #box-interface, #hash-input
**Created:** 2026-01-13
**Type:** code-notes

# generator_bridge

## Summary

```
A dynamic Python generator bridge that loads and executes predefined generator modules based on input hashes and types.
```

## Details

> The `GeneratorBridgeBox` class acts as a middleware between user-provided hash inputs and existing Python generator modules. It dynamically discovers and invokes generator functions (e.g., for "plants," "characters," or "robots") by resolving paths from a base directory (`Generators/`). The system validates inputs, resolves file paths, and executes generators while preserving constraints and returning structured output.
> 
> Key workflows:
> 1. **Path Resolution**: Uses predefined mappings (e.g., `"plants" → "Plants/plants.py"`) or searches recursively for matching `.py` files.
> 2. **Dynamic Execution**: Imports and invokes generator functions via `importlib` after validating file existence.
> 3. **Error Handling**: Logs failures and returns structured `BoxOutput` with success flags and error messages.

## Key Functions

### ``__init__``

Initializes the bridge with a base path to generator modules, ensuring the directory is added to `sys.path`.

### ``execute``

Orchestrates the entire workflow: validates inputs, resolves generator paths, loads modules, and invokes them with hashed input data.

### ``_find_generator_file``

Maps generator types to file paths (e.g., `"characters"` → `"Creatures/Characters/characters.py"`) or performs a recursive search if no mapping exists.

### ``_call_generator``

Dynamically imports and executes the generator function (assumes it follows a naming convention like `generate_<type>(hash, constraints)`).

## Usage

1. **Input Requirements**:
   - `hash`: Required string input (e.g., `"unique_id"`).
   - `generator_type`: Optional type (e.g., `"plants"`) or `generator_path` (absolute/relative path to `.py` file).
   - `constraints`: Optional dictionary for generator-specific parameters.

2. **Example Workflow**:
   ```python
   bridge = GeneratorBridgeBox()
   result = bridge.execute({
       "hash": "abc123",
       "generator_type": "plants"
   })
   ```
   Returns structured output like:
   ```json
   {
       "generated_data": {...},  # Generator output
       "generator_type": "plants",
       "hash": "abc123"
   }
   ```

## Dependencies

> ``os``
> ``sys``
> ``importlib.util``
> ``logging``
> ``typing``
> ``..core.box_interface` (custom BoxInput/BoxOutput classes).`

## Related

- [[`core]]
- [[` directory structure]]

>[!INFO] Dynamic Path Resolution
> The system first checks predefined mappings (e.g., `"characters"` → `"Creatures/Characters/characters.py"`). If no mapping exists, it performs a recursive search for files matching `generator_type.lower() + ".py"` in the base directory.


>[!WARNING] File Naming Assumptions
> Assumes generator files follow the pattern `<type>.py` (e.g., `"plants.py"`). If generators use different naming (e.g., `generate_plants()`), the `_call_generator` method will fail unless explicitly modified to match the expected function signature.
