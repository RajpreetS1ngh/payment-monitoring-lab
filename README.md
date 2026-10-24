# Payment Service Monitoring & Incident Response Lab

Hands-on lab for production monitoring, alerting, and incident response.

## Architecture

Load generator → FastAPI payment API → PostgreSQL

Metrics → Prometheus → Grafana

## Status

~20% complete. Core structure, Docker Compose skeleton, basic FastAPI app, Dockerfile, and CI workflow in place.

## Next steps

- Full metrics instrumentation (prometheus-fastapi-instrumentator)
- Alert rules and Grafana dashboard
- Bash healthcheck/log parser scripts + cron
- Incident reports and runbooks
- Load generator
- Postgres integration and chaos mode
