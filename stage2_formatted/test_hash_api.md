**Tags:** #Flask, #API, #Hashing, #Story-Generation, #Backend, #Python, #Test-Server
**Created:** 2026-01-13
**Type:** code-notes

# test_hash_api

## Summary

```
A Flask-based test server for generating kid-friendly stories using hash-based inputs and linking them to a time-space continuum.
```

## Details

> This server implements a simple POST endpoint (`/api/hash/generate/simple-story`) that takes user-provided inputs (e.g., `storyType`, `heroName`, `heroTraits`, `setting`) to generate a story seed. It uses a hash-based system (via `backend.hash_generation_api`) to produce a structured story, including a linked plot and metadata like characters, locations, and space-time connections. The response includes formatted story text, metadata, and a hash reference for further exploration. A `/health` endpoint provides basic server status checks.

## Key Functions

### `generate_simple_story`

Endpoint that processes user inputs, generates a story seed, and returns a formatted story with linked plot data.

### `health`

Simple GET endpoint to check server health.

## Usage

1. Run the script (`python test_hash_api.py`).
2. Send a POST request to `http://localhost:5001/api/hash/generate/simple-story` with JSON payload:
   ```json
   {
       "storyType": "fantasy",
       "heroName": "Elf",
       "heroTraits": ["Loyal", "Cunning"],
       "setting": "dragon_den"
   }
   ```
3. Expected response includes story text, metadata, and hash-based links.

## Dependencies

> `flask`
> `backend.hash_generation_api`

## Related

- [[backend]]
- [[story-generation-workflow]]

>[!INFO] Input Handling
> Default values (e.g., `storyType='adventure'`, `heroName='Hero'`) are used if inputs are missing. Customize inputs for varied story outcomes.

>[!WARNING] Error Handling
> Unhandled exceptions return a 500 error with the exception trace. Ensure robust input validation in production.
