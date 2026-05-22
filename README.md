# Bio API — Secure Biological Data API

![Security Pipeline](https://github.com/dparedes-sec/bio-api-secure/actions/workflows/security.yml/badge.svg)

> REST API for querying genomic sequence data with JWT authentication,
> role-based access control, and OWASP API Security Top 10 compliance.

---

## Security Features

| Control | Implementation |
|---------|---------------|
| Authentication | JWT Bearer tokens (HS256, configurable expiry) |
| Authorization | RBAC — Admin / Lab Technician / Researcher |
| Input Validation | Pydantic v2 with DNA sequence whitelist (A/C/G/T/N) |
| Rate Limiting | 100 req/min global · 10 req/min on /auth/token |
| Audit Logging | All CRUD events logged — no PII stored |
| Security Headers | CSP · X-Frame-Options · Referrer-Policy · Permissions-Policy |
| Container Security | Non-root user · minimal base image (python:3.12-slim) |

---

## Quick Start

```bash
git clone https://github.com/dparedes-sec/bio-api-secure
cd bio-api-secure
cp .env.example .env
# Set SECRET_KEY in .env
docker-compose up --build
```

API: http://localhost:8000
Docs: http://localhost:8000/docs

---

## OWASP API Security Top 10

See [OWASP_API_CHECKLIST.md](OWASP_API_CHECKLIST.md) for full coverage.

---

## Tech Stack

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---

## Author

**Daniel Paredes** — Developer transitioning into AppSec & DevSecOps | Bioinformatics Security
