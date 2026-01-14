**Tags:** #monitoring, #prometheus, #docker, #flask, #metrics, #alerting, #observability
**Created:** 2026-01-13
**Type:** documentation

# task_023

## Summary

```
Configures Prometheus monitoring for a Flask application via Docker Compose, exposing metrics for latency, errors, and API usage.
```

## Details

> This task outlines setting up Prometheus to monitor a Flask backend application. It involves:
> 1. Adding a Prometheus service to `docker-compose.yml` with persistent storage and proper port mapping.
> 2. Instrumenting the Flask app with `prometheus-flask-exporter` to expose `/metrics` endpoint.
> 3. Configuring Prometheus to scrape metrics from the Flask app and verify real-time updates.

## Key Functions

### ``prometheus.yml``

Scrape configuration for Flask `/metrics` endpoint.

### ``prometheus-flask-exporter``

Exposes Flask metrics via `/metrics` endpoint.

### `Prometheus Docker service`

Scrapes and stores metrics from Flask app.

## Usage

1. Edit `docker-compose.yml` to include Prometheus service with `prometheus.yml` mounted.
2. Install `prometheus-flask-exporter` in Flask app and expose `/metrics`.
3. Configure `prometheus.yml` with `scrape_config` pointing to Flask service.
4. Run `docker-compose up -d` and verify Prometheus UI shows Flask metrics.

## Dependencies

> ``docker-compose``
> ``prometheus/prometheus``
> ``prometheus-flask-exporter` (Flask app environment).`

## Related

- [[Task 23]]
- [[Task 23]]

>[!INFO] Important Note
> Ensure the Flask app’s `/metrics` endpoint is publicly accessible (e.g., via `0.0.0.0`) in `docker-compose.yml` for Prometheus to scrape.

>[!WARNING] Caution
> Misconfigured `prometheus.yml` may cause Prometheus to fail to scrape targets. Test scrape_config incrementally to avoid downtime.
