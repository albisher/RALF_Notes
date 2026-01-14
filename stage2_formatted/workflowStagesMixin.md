**Tags:** #Vue.js, #Workflow Management, #State Management, #Mixin Component, #Data Tracking
**Created:** 2026-01-13
**Type:** code-notes

# workflowStagesMixin

## Summary

```
Manages workflow stage state and navigation for a Vue.js application, tracking progress and completion across predefined stages.
```

## Details

> This mixin initializes a Vue component with predefined workflow stages (`generate`, `link`, `card`, `timeline`, `story`), each containing metadata like `id`, `name`, `icon`, `description`, `type`, `count`, and `completed` status. The component provides methods to:
> - Switch between stages via `switchStage()`.
> - Update stage progress counts via `updateStageCount()`.
> - Mark stages as completed via `setStageCompleted()`.
> Logging is used for debugging transitions and errors.

## Key Functions

### ``switchStage(stageId)``

Updates `currentStage` to a specified stage ID, logging the transition.

### ``updateStageCount(stageId, count)``

Modifies the `count` property of a stage by its ID.

### ``setStageCompleted(stageId, completed)``

Sets the `completed` flag for a stage by its ID.

## Usage

To use this mixin in a Vue component:
```javascript
import workflowStagesMixin from './mixins/workflowStagesMixin';

export default {
    mixins: [workflowStagesMixin],
    // Component logic can interact with `currentStage`, `workflowStages`, etc.
};
```
Call methods like:
```javascript
this.switchStage('card'); // Navigate to 'card' stage
this.updateStageCount('card', 5); // Update 'card' stage count
```

## Dependencies

> ``../utils/logger.js` (for debugging/error logging)`

## Related

- [[Vue]]
- [[State Management Patterns in Vue]]

>[!INFO] Initial State
> Stages are initialized with default values (e.g., `count: 0` for `generate`/`story`, `count: 4` for `card`). Hardcoded values may need adjustment for dynamic workflows.

>[!WARNING] Immutable Updates
> `updateStageCount()`/`setStageCompleted()` uses `find()` to modify stages in-place. For immutable state, consider returning a new array or using Vue’s reactivity carefully.
