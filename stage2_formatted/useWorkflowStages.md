**Tags:** #Vue.js, #Composable, #Workflow Management, #State Management, #Stage Navigation
**Created:** 2026-01-13
**Type:** documentation

# useWorkflowStages

## Summary

```
Manages workflow stages with state tracking and navigation for a Vue.js application.
```

## Details

> This composable (`useWorkflowStages`) provides a reactive way to handle workflow stages, including tracking the current stage, managing stage counts, and tracking completion statuses. It initializes a predefined list of stages with IDs, names, icons, descriptions, and metadata (e.g., `count`, `completed`). The core logic includes:
> - **State tracking**: `currentStage` ref holds the active stage (default: `'generate'`).
> - **Navigation**: `switchStage()` validates and updates the current stage via ID.
> - **Data updates**: `updateStageCount()` and `setStageCompleted()` modify stage-specific metadata (e.g., incrementing `count` or toggling `completed`).
> - **Logging**: Debug/error logs track transitions and invalid inputs.

## Key Functions

### ``switchStage(stageId)``

Changes the active workflow stage after validation.

### ``updateStageCount(stageId, count)``

Updates the completion count for a stage.

### ``setStageCompleted(stageId, completed)``

Marks a stage as completed/incomplete.

### ``currentStage``

Reactive ref tracking the active stage ID.

### ``workflowStages``

Immutable ref of all defined stages (array of objects).

## Usage

```javascript
import { useWorkflowStages } from './composables/useWorkflowStages';

const { currentStage, workflowStages, switchStage, updateStageCount, setStageCompleted } = useWorkflowStages();

// Example: Navigate to 'card' stage
switchStage('card');

// Example: Update 'card' stage count to 5
updateStageCount('card', 5);

// Example: Mark 'timeline' stage as completed
setStageCompleted('timeline', true);
```

## Dependencies

> ``vue``
> ``vuex` (implicitly via `ref`/`computed`)`
> ``@mdi/core` (for icons)`
> ``../utils/logger.js` (custom logger).`

## Related

- [[Vue]]
- [[Workflow State Patterns]]
- [[Reactive Data Management]]

>[!INFO] Default Stage
> The `currentStage` defaults to `'generate'` (ID: `'generate'`). Override this in the composable’s initialization if needed.

>[!WARNING] Immutable Stages
> `workflowStages` is a ref of an array; modifications (e.g., `updateStageCount`) must use `.value` (e.g., `workflowStages.value.find(...)`). Direct array access will fail.

>[!INFO] Validation
> `switchStage()` rejects invalid IDs via `logger.error()`. Always validate `stageId` before calling.
