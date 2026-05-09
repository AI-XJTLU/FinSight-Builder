# Deployment Notes

Application: FinSight Builder educational stock watchlist and risk briefing.

Local test command:

```powershell
python -m pytest Task1/artifacts/app/tests
```

Docker deployment command:

```powershell
docker compose -f Task1/artifacts/app/docker-compose.yml up --build
```

Expected URLs:
- Website: `http://127.0.0.1:5005/`
- Health API: `http://127.0.0.1:5005/health`
- Stock API: `http://127.0.0.1:5005/api/stocks`

Captured evidence:
- Git commit history evidence: `screenshots/01_commit_records.png`.
- Docker deployed website screenshot showing the generated banner: `screenshots/02_docker_deployed_website.png`.
- API JSON evidence: `screenshots/04_api_health_or_stocks_optional.png`.
- Docker container/log evidence: `screenshots/05_docker_container_optional.png`.

Evidence still to capture after GitHub access is restored:
- GitHub Actions success screenshot: `screenshots/03_github_actions_success.png`.

Current verification status:
- Local pytest passed: 6 tests passed.
- The notebook was executed successfully using the Python environment located under `anaconda3\envs\ai_in_se_cw`.
- Local Flask runtime check passed: `/health`, `/api/stocks`, and `/` each returned HTTP 200 from `http://127.0.0.1:5005`.
- Docker Compose deployment passed after pulling `docker.m.daocloud.io/python:3.11-slim`, tagging it as `python:3.11-slim`, and running `docker compose -f Task1/artifacts/app/docker-compose.yml up --build -d`.
- Docker container evidence, website evidence, API evidence, pytest output, and runtime logs are saved under `screenshots/` and `test_results/`.
- Local Git contains seven meaningful commits, but pushing to GitHub is currently blocked by local access configuration: SSH returns `Permission denied (publickey)`, HTTPS direct access is reset, and the configured proxy `127.0.0.1:7890` is not listening.
