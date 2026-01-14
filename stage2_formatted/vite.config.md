**Tags:** #Vite, #Vue.js, #Webpack, #Proxying, #Development-Server
**Created:** 2026-01-13
**Type:** code-configuration

# vite.config

## Summary

```
Configures Vite for a Vue.js project with Vuetify optimization and API proxying.
```

## Details

> This `vite.config.js` sets up a Vite development server for a Vue.js application. It includes:
> - A **Vue plugin** for Vue.js support.
> - **Alias resolution** for internal imports (e.g., `@` → `src`).
> - **Optimized dependencies** for Vuetify to reduce bundle size.
> - **Server configuration** with:
>   - Hosting on `0.0.0.0` and port `5173`.
>   - HMR (Hot Module Replacement) on `localhost:5173`.
>   - A proxy for `/api` to forward requests to `http://backend:5000`.

## Key Functions

### ``defineConfig``

Core Vite configuration function.

### ``vue()``

Vite plugin for Vue.js support.

### ``resolve.alias``

Maps `@` to `src` for internal imports.

### ``optimizeDeps.include``

Pre-bundles Vuetify for performance.

### ``server.proxy``

Routes `/api` requests to a backend service.

## Usage

1. Install dependencies (`npm install`).
2. Run with `npm run dev` to start the dev server.
3. Access the app at `http://localhost:5173` and proxy API calls via `/api`.

## Dependencies

> ``vite``
> ``@vitejs/plugin-vue``
> ``node:url``
> ``vuetify``

## Related

- [[Vite Documentation]]
- [[Vue]]

>[!INFO] **Proxy Behavior**
> Requests to `/api` are rewritten to `http://backend:5000` without modifying the path (e.g., `/api/users` → `/users`).

>[!WARNING] **Security Note**
> `secure: false` in the proxy may expose sensitive data if the backend lacks HTTPS. Use `secure: true` in production.
