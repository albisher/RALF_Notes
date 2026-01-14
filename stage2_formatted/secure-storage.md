**Tags:** #SecureStorage, #TokenManagement, #Encryption, #LocalStorage, #WebCrypto
**Created:** 2026-01-13
**Type:** code-library

# secure-storage

## Summary

```
Secure token storage with basic encryption and expiration handling for sensitive data.
```

## Details

> This library implements a secure storage mechanism using localStorage for token storage, with encryption via a simple XOR cipher (for demonstration; production should use Web Crypto API). It manages tokens with expiration, key-based access, and cleanup methods. The system relies on `localStorage` exclusively, with no sessionStorage fallback, and includes error logging via a logger module.

## Key Functions

### ``_getOrCreateEncryptionKey()``

Retrieves or generates a 32-byte random key stored in `sessionStorage` (cleared on browser close).

### ``_generateKey()``

Creates a hex-encoded random key (basic implementation; production should use secure key derivation).

### ``_encrypt(text, key)``

Simple XOR encryption converting text to a hex string for storage.

### ``_decrypt(encrypted, key)``

Reverses XOR encryption from hex input.

### ``setToken(key, value, expirationMs)``

Stores an encrypted token with an optional expiration time (default: 24 hours).

### ``getToken(key)``

Retrieves and decrypts a token, returning `null` if expired or invalid.

### ``removeToken(key)``

Deletes a token from `localStorage`.

### ``hasToken(key)``

Checks if a token exists and is valid.

### ``clearAll()``

Removes all tokens prefixed with `spq8_` from `localStorage`.

## Usage

1. Import the exported `secureStorage` instance.
2. Call `setToken(key, value, expirationMs)` to store a token.
3. Retrieve with `getToken(key)`.
4. Clean up with `removeToken(key)` or `clearAll()`.

## Dependencies

> ``logger` (from `./logger.js`)`
> ``crypto` (built-in browser API for randomness).`

## Related

- [[SecureStorage_ProductionGuide]]
- [[WebCrypto_API_Comparison]]

>[!INFO] Key Storage Limitation
> The encryption key is stored in `sessionStorage`, which is cleared on browser closure. For persistence, consider using `localStorage` or a secure cookie.

>[!WARNING] XOR Encryption Weakness
> The XOR cipher is trivial to break. In production, replace with Web Crypto API (e.g., AES-GCM) for cryptographic security.

>[!WARNING] LocalStorage Quotas
> `localStorage` has a 5MB limit per origin. Tokens should be small or use chunking for large payloads.
