# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 1.x.x   | Yes       |

## Reporting a vulnerability

If you discover a security vulnerability, please report it privately:

1. Go to the Security tab of this repository
2. Click 'Report a vulnerability'
3. Provide a description, steps to reproduce, and potential impact

Do not open public issues for security vulnerabilities.

## Security controls implemented

- JWT authentication with configurable expiration
- Role-based access control (Admin, Lab Technician, Researcher)
- Pydantic input validation with DNA sequence whitelist
- Per-IP rate limiting on all endpoints
- Comprehensive audit logging (no PII stored)
- HTTP security headers (CSP, X-Frame-Options, Referrer-Policy)
- Non-root Docker container execution
- Parameterized queries via SQLAlchemy ORM
