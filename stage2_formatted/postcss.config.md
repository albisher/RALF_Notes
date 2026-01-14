**Tags:** #PostCSS, #CSS, #TailwindCSS, #Autoprefixer, #Build-Tools
**Created:** 2026-01-13
**Type:** configuration

# postcss.config

## Summary

```
Configures PostCSS plugins for Tailwind CSS and Autoprefixer in a build process.
```

## Details

> This file exports a default configuration for PostCSS, defining two plugins: `tailwindcss` (for utility-first styling) and `autoprefixer` (for adding vendor prefixes). The configuration is typically used in build pipelines (e.g., Webpack, Vite) to process CSS files with these plugins.

## Key Functions

### ``tailwindcss``

Applies Tailwind CSS classes to HTML/CSS output.

### ``autoprefixer``

Automatically adds browser-specific prefixes to CSS properties.

## Usage

1. Import this config in a build setup (e.g., `postcss.config.js`).
2. Use in a bundler like Webpack/Vite with:
   ```js
   module.exports = {
     plugins: [require('postcss-import'), require('./postcss.config')],
   };
   ```
3. Ensure `tailwindcss` and `autoprefixer` are installed globally or in the project.

## Dependencies

> `PostCSS`
> ``tailwindcss-plugin-tailwindcss``
> ``autoprefixer` (external npm packages).`

## Related

- [[none]]

>[!INFO] Common Use Case
> This config is often paired with a Tailwind CSS setup where `tailwindcss` processes CSS files into utility classes, and `autoprefixer` ensures compatibility across browsers.

>[!WARNING] Dependency Risk
> Missing `autoprefixer` or `tailwindcss` will cause build failures. Always install them explicitly.
