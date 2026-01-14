### TAGS
#data-conversion
#api-integration
#database-migration
#mock-to-real
#backend-script

### TYPE
documentation

### SUMMARY
Script converts mock card data from a JSON file into real database entries via backend API.

### DETAILS
This script automates the process of migrating mock card data from `ui-beta/data/cards-data.js` into a backend database by reformatting and submitting each card via an API endpoint. It handles data mapping, duplicate checks, and progress reporting while allowing customization of the world ID and API endpoint.

### KEY_FUNCTIONS
- **`load_mock_cards()`**: Extracts and parses mock card data from `cards-data.js`.
- **`fetch_world_id()`**: Retrieves the world ID from the API (defaults to first available if not specified).
- **`convert_card_data()`**: Maps mock card attributes (`name`, `type`, `description`, etc.) to API-compatible fields.
- **`check_duplicate()`**: Skips cards with existing names in the specified world.
- **`create_card()`**: Submits converted card data to the API (`POST /api/cards`).
- **`report_progress()`**: Logs real-time processing status and final summary.

### DEPENDENCIES
`requests`, `docker-compose` (for backend service), backend API (running at `http://localhost:5001/api`).

### USAGE
1. Ensure the backend API is running (`docker-compose up -d backend`).
2. Run the script with optional arguments:
   - `WORLD_ID=1` (specify a world ID).
   - `API_BASE_URL=http://localhost:5001/api` (override default API endpoint).
3. Execute via Python:
   ```bash
   python3 scripts/convert_mock_cards_to_real.py
   ```

### RELATED
[[Troubleshooting Guide for API Failures]], [[Backend API Documentation]], [[Mock Card Data Format Specification]]

### CALLOUTS
>[!INFO]- **Duplicate Handling**
> Cards with identical names in the same world are skipped to avoid duplicates. This is enforced via `check_duplicate()` before API submission.
>[!WARNING]- **Error Resilience**
> Failed cards are logged but do not halt execution. The script continues processing remaining cards even if some API calls fail, ensuring partial success.
>[!INFO]- **World Dependency**
> Requires at least one world in the database. If none exists, the script will fail unless a world is created beforehand. Verify with `curl http://localhost:5001/api/worlds`.