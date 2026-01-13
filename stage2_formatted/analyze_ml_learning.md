**Tags:** #machine-learning, #data-analysis, #session-tracking, #json-processing, #defaultdict
**Created:** 2026-01-13
**Type:** code-notes

# analyze_ml_learning

## Summary

```
Analyzes machine learning session data to extract learned patterns, decision trends, and performance metrics.
```

## Details

> This script loads and aggregates data from multiple training sessions stored in a directory structure. It reads JSON files containing ML training data, simulation summaries, motion history, and detection data for each session. The `load_session_data` function retrieves all available data for a given session ID, while `analyze_what_learned` processes this data to identify recurring decision patterns, outcomes, and performance improvements across sessions. The analysis uses `defaultdict` to track patterns dynamically and compiles structured results into a dictionary.

## Key Functions

### `load_session_data(session_id`

str)**: Loads all JSON files (ML data, summary, motion history, detection) from a session directory into a unified dictionary.

### `analyze_what_learned(session_data`

List[Dict])**: Aggregates decision patterns, outcomes (e.g., mission success, buildings scouted/cleaned), and performance trends across sessions.

## Usage

1. Define `TRAINING_SESSIONS_DIR` pointing to the directory containing session folders.
2. Call `load_session_data(session_id)` to fetch session data.
3. Call `analyze_what_learned()` with a list of session dictionaries to generate insights.
4. Output is a structured dictionary with patterns, outcomes, and trends.

## Dependencies

> `numpy`
> `pathlib`
> `collections.defaultdict`
> `json`

## Related

- [[none]]

>[!INFO] Important Note
> The script gracefully handles missing files by returning `None` for unloaded fields (e.g., `ml_data`, `summary`) and skips JSON parsing errors silently.

>[!WARNING] Caution
> Ensure session directories exist and contain required JSON files (e.g., `ml_training_data.json`, `simulation_summary.json`) to avoid silent failures.
