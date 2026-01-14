**Tags:** #nginx-configuration, #api-urls, #card-conversion, #docker-compose, #backend-api, #frontend-ui, #mock-to-real-conversion, #health-check, #troubleshooting
**Created:** 2026-01-13
**Type:** documentation

# BETA_SETUP_COMPLETE

## Summary

```
Documentation for beta setup completion, including Nginx configuration, API URL updates, and card conversion scripts for a development environment.
```

## Details

> This document outlines the completion of a beta setup process, focusing on fixing Nginx configurations to serve the UI-beta, updating API URLs to use HTTP via Nginx proxy, and implementing a script to convert mock cards into real database entries. The setup includes Docker-based services, configuration adjustments for static files and proxy, and verification steps to ensure functionality.

## Key Functions

### ``convert_mock_cards_to_real.py``

Converts mock card data from `ui-beta/data/cards-data.js` into real database entries, handling duplicates and reporting progress.

### ``nginx/static-files.conf``

Configures Nginx to serve static files for `/ui-beta/`, `/app/`, and `/ui-explorations/` directories.

### ``nginx/default.conf``

Updates proxy rules to route `/ui-beta/` requests to the static-files container.

### ``ui-beta/js/api-client.js``

Adjusts API client to use `http://localhost:8888/api` via Nginx proxy.

### ``docker-compose.yml``

Includes volumes for static files and updated health checks for containers.

## Usage

1. **Setup**:
   - Run `docker-compose up -d backend` to start the backend service.
   - Execute `python3 scripts/convert_mock_cards_to_real.py` to convert mock cards.
   - Update API client and Nginx configs as per the provided scripts.

2. **Access**:
   - Primary UI: `http://localhost:8888/ui-beta/`
   - Backend API: `http://localhost:8888/api` (via proxy) or `http://localhost:5001/api` (direct).

3. **Verification**:
   - Check services with `docker-compose ps`.
   - Test UI with `curl http://localhost:8888/ui-beta/`.
   - Test API with `curl http://localhost:8888/api/worlds`.

## Dependencies

> `docker-compose`
> `Nginx`
> `Python 3`
> `backend API service (running on `localhost:5001`)`
> `static-files container`
> `frontend Vue Dev (running on `localhost:5173`).`

## Related

- [[Beta Setup Guide]]
- [[Nginx Configuration Guide]]
- [[Docker Compose Setup]]
- [[API Documentation]]

>[!INFO] Important Note
> Ensure the backend is running before running the card conversion script. The script relies on the backend API to process card data, so a failed backend will cause the conversion to fail.


>[!WARNING] Caution
> If the world ID is not set correctly, the script will default to the first available world. Manually setting `WORLD_ID` in the environment variables can prevent unexpected behavior during conversion.
