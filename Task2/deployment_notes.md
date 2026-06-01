# FinSight Builder Deployment Notes

Run these commands from the repository root after reviewing the generated artifacts.

## Local tests

```powershell
python -m pytest Task1/artifacts/app/tests -q
```

Save real output to `Task2/test_results/pytest_output.txt` only after the command has been run.

## Run Flask locally

```powershell
python Task1/artifacts/app/flask/main.py
```

Open:

```text
http://127.0.0.1:5005/
http://127.0.0.1:5005/health
http://127.0.0.1:5005/api/stocks
```

## Run with Docker Compose

```powershell
docker compose -f Task1/artifacts/app/docker/docker-compose.yml up --build
```

Open `http://127.0.0.1:5005/` and capture real screenshots only after the container is running.

Stop the container with:

```powershell
docker compose -f Task1/artifacts/app/docker/docker-compose.yml down
```

## GitHub Actions

Use `Task2/github_workflow_copy/ci.yml` as the generated workflow copy. A success screenshot should be added only after the workflow has run on GitHub.

## Manual screenshot checklist

Capture screenshots manually after the current version has been pushed and deployed:

1. GitHub commit history for version-control evidence.
2. Docker-served dashboard at `http://127.0.0.1:5005/`, with the generated banner visible.
3. Successful GitHub Actions workflow run showing pytest and Docker build steps.
4. Recommended: `/health` or `/api/stocks` JSON response.
5. Recommended: Docker Desktop container state or `docker compose ps` output.
