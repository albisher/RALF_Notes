**Tags:** #story-generation, #card-creation, #backend-integration, #randomization, #data-structures
**Created:** 2026-01-13
**Type:** code-script

# create_story_100_cards

## Summary

```
Generates 100+ themed story cards with randomized attributes for testing narrative systems.
```

## Details

> This script automates the creation of 100+ story-related cards (e.g., characters, locations, items) using predefined categories (e.g., `plants`, `buildings`, `dragons`) and combines them with adjectives/nouns. It integrates with a backend API to authenticate, fetch/create a world, and post cards. The script handles authentication, random selection from predefined lists, and error handling for API calls.
> 
> The `generateStoryCards()` function iterates through a loop, selecting random card types/subtypes, generating names with adjectives/nouns, and constructing descriptions. It tracks success/failure counts and logs progress.

## Key Functions

### `login()`

Authenticates with the backend API using provided credentials.

### `getOrCreateWorld()`

Checks for an existing world or creates a new one named "Story World - 100 Cards Test."

### `generateRandomHash(prefix)`

Generates a cryptographic hash for unique identifiers.

### `getRandomElement(array)`

Randomly selects an element from an array.

### `createCard(cardData)`

Posts a card to the backend API with the provided data.

### `generateStoryCards(count)`

Orchestrates the creation of `count` story cards by:

## Usage

1. Set environment variables (`BACKEND_URL`, `USERNAME`, `PASSWORD`) or use defaults.
2. Run the script to authenticate, create a world, and generate 100+ story cards.
3. Cards are stored in the backend API under the created world.

## Dependencies

> `axios`
> `crypto`

## Related

- [[backend-api-documentation]]
- [[story-card-template]]

>[!INFO] Authentication Fallback
> If `process.env` credentials fail, the script defaults to `USERNAME = 'a'` and `PASSWORD = 'spq8'`. Ensure these are secure or adjust environment variables.

>[!WARNING] API Rate Limits
> Frequent API calls may trigger rate limits. Monitor backend logs for errors during execution.
