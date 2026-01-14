**Tags:** #ContentSecurityPolicy, #VueJS, #Nginx, #CSPFix, #WebSecurity, #DevelopmentMode, #DockerCompose
**Created:** 2026-01-13
**Type:** documentation

# csp_fix_complete

## Summary

```
Fixes Vue.js application CSP errors by updating Nginx CSP headers to allow `'unsafe-eval'` for development.
```

## Details

> This document details the implementation of a CSP fix for a Vue.js application that was failing due to overly restrictive Nginx CSP headers. The root issue was that `'unsafe-eval'` was missing, which Vue.js requires for dynamic evaluation in development mode. The solution involved modifying the Nginx configuration to explicitly include `'unsafe-eval'` in critical directives (`default-src`, `script-src`, `style-src`) while maintaining security. The fix was verified via HTTP and browser tests to confirm the application loads correctly.

## Key Functions

### ``nginx/nginx.conf``

Modified CSP header directives to include `'unsafe-eval'`.

### ``docker-compose down/up -d``

Restarted containers with updated configurations.

### ``curl -k -I https`

//localhost:8443/login`: Verified CSP header inclusion via HTTP request.

### ``checks/simple-browser-test.js``

Created a Puppeteer test to validate browser compatibility.

## Usage

1. Edit `nginx/nginx.conf` to update CSP headers as shown.
2. Stop and restart containers with `docker-compose down` followed by `docker-compose up -d`.
3. Verify fixes using `curl` or browser tests.

## Dependencies

> `nginx`
> `Docker`
> `Docker Compose`
> `curl`
> `Puppeteer (for browser testing)`

## Related

- [[CSP Best Practices Guide]]
- [[Vue]]
- [[Nginx Configuration Reference]]

>[!INFO] Important Note
> The `'unsafe-eval'` directive is only for development. In production, remove it and use a production-ready Vue.js build to eliminate CSP conflicts.

>[!WARNING] Caution
> Overly permissive CSP headers can expose applications to security risks. Always balance security with functionality during development.
