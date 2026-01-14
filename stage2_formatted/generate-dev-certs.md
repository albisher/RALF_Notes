**Tags:** #SSL, #Certificates, #Development, #Self-Signed, #Bash-Script
**Created:** 2026-01-13
**Type:** code-notes

# generate-dev-certs

## Summary

```
Generates self-signed SSL certificates for local development environments.
```

## Details

> This script automates the creation of a self-signed SSL certificate and private key using OpenSSL, configured for local development (e.g., `localhost` and `127.0.0.1`). It ensures the directory `nginx/ssl` exists before generating the files, which are stored in `cert.pem` (certificate) and `key.pem` (private key). The certificate is valid for 365 days and includes an extended key usage (EKU) for TLS/SSL.

## Key Functions

### ``openssl req``

Generates a self-signed certificate with specified parameters.

### ``mkdir -p nginx/ssl``

Creates the directory structure for storing SSL files if it doesn’t exist.

## Usage

1. Save the script as `generate-dev-certs.sh`.
2. Run it with `./generate-dev-certs.sh` in the directory containing the `nginx/ssl` folder.
3. Use the generated files (`cert.pem`, `key.pem`) in an Nginx or other web server configuration for HTTPS testing.

## Dependencies

> `OpenSSL`
> `Bash shell.`

## Related

- [[none]]

>[!INFO] Important Note
> Ensure the script is executed in a directory where `nginx/ssl` already exists or the script will fail. The generated files are only valid for local testing (e.g., `localhost` or `127.0.0.1`).

>[!WARNING] Caution
> Self-signed certificates are not trusted by default in browsers. Test locally or configure your system to trust the certificate (e.g., via browser exceptions or OS CA store).
