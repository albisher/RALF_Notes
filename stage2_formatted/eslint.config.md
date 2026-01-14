**Tags:** #ESLint, #Vue.js, #TypeScript, #Configuration, #Linting
**Created:** 2026-01-13
**Type:** configuration

# eslint.config

## Summary

```
Configures ESLint for a Vue.js/TypeScript project with file-specific rules and global ignores.
```

## Details

> This file defines an ESLint configuration using the `@vue/eslint-config-typescript` plugin, targeting `.ts`, `.mts`, `.tsx`, and `.vue` files. It applies Vue-specific rules via `pluginVue.configs['flat/essential']` and TypeScript recommendations (`vueTsConfigs.recommended`). Global ignores exclude build artifacts (`dist/`, `dist-ssr/`, `coverage/`). The `skipFormatting` plugin prevents formatting conflicts with Prettier. The commented-out `configureVueProject` suggests extending script language support beyond TypeScript if needed.

## Key Functions

### ``defineConfigWithVueTs``

Core Vue ESLint config wrapper.

### ``globalIgnores``

Excludes specified directories from linting.

### ``pluginVue.configs['flat/essential']``

Applies Vue-specific linting rules.

### ``vueTsConfigs.recommended``

Enforces TypeScript best practices.

### ``skipFormatting``

Disables formatting checks (Prettier integration).

## Usage

1. Install dependencies:
   ```bash
   npm install --save-dev eslint @vue/eslint-config-typescript eslint-plugin-vue @vue/eslint-config-prettier/skip-formatting
   ```
2. Place this file in your project’s ESLint config directory (e.g., `.eslintrc.js`).
3. Run ESLint with:
   ```bash
   npx eslint .
   ```

## Dependencies

> ``eslint/config``
> ``@vue/eslint-config-typescript``
> ``eslint-plugin-vue``
> ``@vue/eslint-config-prettier/skip-formatting``

## Related

- [[ESLint Plugin Vue Docs]]
- [[Vue ESLint TypeScript Guide]]

>[!INFO] **Global Ignores**
> Excludes `dist/` and `coverage/` to avoid linting build outputs, improving performance.

>[!WARNING] **Prettier Conflict**
> `skipFormatting` must be used *after* Prettier integration to prevent conflicts. Ensure Prettier is also configured in the project.
