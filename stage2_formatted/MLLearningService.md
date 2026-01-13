**Tags:** #MachineLearning, #APIService, #DataExport, #OOP, #DependencyInjection
**Created:** 2026-01-13
**Type:** code-notes

# MLLearningService

## Summary

```
Handles machine learning data fetching, exporting, and training operations via HTTP API calls.
```

## Details

> `MLLearningService` is a class-based service implementing single responsibility for managing ML data operations. It uses dependency injection (via `APIBox`) for HTTP communication. The service provides methods to fetch raw ML data, export filtered datasets, retrieve training scenarios, initiate training sessions, and retrieve performance statistics. Error handling is centralized with logging and re-throwing exceptions.

## Key Functions

### ``constructor(apiBox)``

Initializes the service with an `APIBox` instance, validating its presence.

### ``fetchMLLearningData()``

Asynchronously retrieves ML learning data via a GET request to `/api/ml-learning/data`.

### ``exportSelectedMLData(droneNames, format)``

Exports filtered ML data (by drone names) in specified format (default: JSON) via a POST request.

### ``getTrainingScenarios()``

Fetches available training scenarios via a GET request to `/api/ml-learning/scenarios`.

### ``startTrainingSession(config)``

Initiates a training session with provided configuration via a POST request.

### ``getTrainingStatistics()``

Retrieves training performance metrics via a GET request to `/api/ml-learning/statistics`.

## Usage

```javascript
const apiBox = new APIBox(); // Assume this is configured elsewhere
const mlService = new MLLearningService(apiBox);

// Fetch data
const data = await mlService.fetchMLLearningData();

// Export data
const exportResult = await mlService.exportSelectedMLData(['Drone1', 'Drone2'], 'csv');

// Get scenarios
const scenarios = await mlService.getTrainingScenarios();

// Start training
const trainingResult = await mlService.startTrainingSession({ /* config */ });

// Get stats
const stats = await mlService.getTrainingStatistics();
```

## Dependencies

> `APIBox`

## Related

- [[APIBox Documentation]]
- [[ML Data API Specifications]]

>[!INFO] Dependency Validation
> The constructor enforces that `APIBox` must be provided; omitting it throws an error immediately.


>[!WARNING] Error Handling
> Some methods (e.g., `getTrainingStatistics`) return an empty array on failure instead of throwing, which may mask issues. Consider consistent error handling.
