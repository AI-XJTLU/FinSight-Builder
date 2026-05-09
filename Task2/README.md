# Task2 Deployment Evidence

This folder stores evidence for version control, testing, CI/CD, and deployment.

Required screenshots:
- `screenshots/01_commit_records.png`
- `screenshots/02_docker_deployed_website.png`
- `screenshots/03_github_actions_success.png`

Recommended extra evidence:
- `screenshots/04_api_health_or_stocks_optional.png`
- `screenshots/05_docker_container_optional.png`
- `test_results/pytest_output.txt`

Run locally from the repository root:

```powershell
python -m pytest Task1/artifacts/app/tests
docker compose -f Task1/artifacts/app/docker-compose.yml up --build
```

Current local verification:
- `python -m pytest Task1/artifacts/app/tests` passes locally; the saved output is in `test_results/pytest_output.txt`.
- Local Flask endpoint checks pass for `/health`, `/api/stocks`, and `/`.
- Docker Compose deployment passes locally after pulling `python:3.11-slim` through a working registry mirror and tagging it as the standard base image. Container and endpoint evidence are saved in `test_results/` and `screenshots/`.
