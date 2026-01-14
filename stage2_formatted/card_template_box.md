**Tags:** #card-template, #box-interface, #data-management, #template-customization, #timeline-view
**Created:** 2026-01-13
**Type:** documentation

# card_template_box

## Summary

```
Manages predefined card visual templates and their customization for dynamic UI adjustments.
```

## Details

> This module implements a `CardTemplateBox` class inheriting from `Box`, providing a structured way to handle card template definitions and modifications. It includes four built-in templates (`compact`, `detailed`, `visual_focused`, `timeline_optimized`) with metadata like field requirements and layout types. The `execute()` method processes three operations: listing all templates, retrieving a specific template by ID, or customizing an existing template with user-provided modifications.

## Key Functions

### ``CardTemplateBox.__init__()``

Initializes the box with predefined template configurations.

### ``execute(input_data`

BoxInput) -> BoxOutput`**:

## Usage

1. **List Templates**: Call with `operation="list"` to retrieve all available templates.
   ```python
   input_data = {"operation": "list"}
   output = box.execute(input_data)
   ```
2. **Get Template**: Fetch a template by ID (e.g., `"compact"`).
   ```python
   input_data = {"operation": "get", "template_id": "compact"}
   output = box.execute(input_data)
   ```
3. **Customize Template**: Modify a template’s fields with `customization` dict.
   ```python
   input_data = {
       "operation": "customize",
       "template_id": "detailed",
       "customization": {"image": "new_path"}
   }
   output = box.execute(input_data)
   ```

## Dependencies

> ``..core.box_interface` (Box`
> `BoxInput`
> `BoxOutput)`
> ``logging` (for error logging).`

## Related

- [[`core.box_interface]]
- [[`card_template_usage.md` (if documentation exists for template integration).]]

>[!INFO] Template Validation
> All operations validate `template_id` existence before processing. Missing IDs return `success=False` with an error message.

>[!WARNING] Immutable Defaults
> Templates are copied during customization to avoid unintended side effects on the original data structure.
