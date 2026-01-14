**Tags:** #world-building, #docker, #ai-integration, #procedural-generation, #vuejs, #flask, #postgresql, #offline-first, #multilingual, #pwa, #storytelling
**Created:** 2026-01-13
**Type:** architecture-documentation

# prd

## Summary

```
A Docker-based Space Pearl universe world-building platform for writers, combining procedural generation, AI assistance, and offline-first capabilities.
```

## Details

> The **Space Pearl World-Building Web Application** is a Dockerized system designed for writers to create, manage, and visualize complex fictional worlds. It leverages Python (Flask) for deterministic procedural generation via hash algorithms, Vue.js for a responsive frontend, and PostgreSQL/Redis for data persistence. Core features include AI-assisted content creation, interactive maps (SVG/D3.js and Three.js), timelines (Pinia + D3.js), and offline-first sync via PWA. The architecture supports multilingual RTL (Arabic-first) and supports exporting/importing in multiple formats (JSON, PDF, Markdown, etc.).

## Key Functions

### `Vue.js SPA`

Handles UI rendering with RTL support, AI suggestions, and real-time updates.

### `Flask REST API`

Exposes CRUD endpoints for world elements (characters, locations, etc.) and integrates AI services.

### `Procedural Generation`

Python backend generates world elements deterministically via hash-based keys.

### `PWA Service Worker`

Enables offline-first functionality with cached data syncing.

### `PostgreSQL + SQLAlchemy`

Manages relational data for world elements, relationships, and audit logs.

### `Docker Compose`

Orchestrates microservices (frontend, backend, database, Redis, Nginx).

### `AI Integration`

Supports local (Ollama) and cloud AI models via Flask endpoints with rate limiting.

## Usage

1. Deploy via Docker Compose (`docker-compose up`).
2. Access the PWA frontend at `http://localhost` (HTTPS via Nginx/Certbot).
3. Create worlds, generate elements procedurally or manually, and visualize via maps/timelines.
4. Export projects (JSON/PDF/Markdown) or sync offline data when online.

## Dependencies

> `Vue.js 3.5.13`
> `Vuetify 3.6.7`
> `Tailwind CSS 3.4.17`
> `Flask 3.0.2`
> `Python 3.12+`
> `PostgreSQL 16`
> `Redis`
> `OpenPyXL`
> `ReportLab`
> `python-docx`
> `D3.js`
> `Three.js`
> `Pinia`
> `Vue Router`
> `Vue I18n`
> `Docker`
> `Nginx`
> `Certbot`
> `Prometheus.`

## Related

- [[Space Pearl Universe Documentation]]
- [[Dockerized World-Builder Architecture]]
- [[Vue]]
- [[PostgreSQL + SQLAlchemy ORM Guide]]
- [[PWA Offline-First Patterns]]

>[!INFO] **Deterministic Generation**
> Hash-based generation ensures reproducible world elements across sessions, critical for consistency in long-term projects.

>[!WARNING] **AI Privacy**
> Local AI (Ollama) is recommended for sensitive data; cloud AI requires user consent and rate limits enforced server-side.
