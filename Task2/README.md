# Task2 Deployment and Evidence

This folder stores evidence for the Software component: version control, testing, CI/CD, and deployment. Evidence must be real screenshots or real command output; do not fabricate missing screenshots.

## Mandatory Evidence

| File | Status | What the screenshot must show |
|---|---|---|
| `screenshots/01_commit_records.png` | Present, but recapture manually if it does not show the GitHub commits page clearly. | GitHub repository commit history with meaningful project commits visible. |
| `screenshots/02_docker_deployed_website.png` | Present; should be refreshed after the latest local deployment if the visual design changes. | Browser URL at `localhost` or `127.0.0.1`, current FinSight Builder hero, generated banner, 9 pytest checks metric, stock cards, risk summary, and API Evidence section if visible. |
| `screenshots/03_github_actions_success.png` | Mandatory pending manual capture. | GitHub Actions workflow with a successful green check; open the run details so pytest and Docker build steps are visible if possible. |

## Optional Supporting Evidence

| File | Status | What the screenshot should show |
|---|---|---|
| `screenshots/04_api_health_or_stocks_optional.png` | Present; recapture if the response is unclear. | Browser URL or terminal command for `/health` or `/api/stocks`, plus readable JSON response. |
| `screenshots/05_docker_container_optional.png` | Present; clean `docker compose ps` or Docker Desktop running-container view is preferred. | Container/service running without messy logs or control characters. |
| `test_results/pytest_output.txt` | Present. | UTF-8 pytest output showing the actual command and `9 passed`. |
| `test_results/website_interaction_check.txt` | Present. | Real local HTTP verification for homepage, generated image reference, stock/risk APIs, watchlist submission, feedback submission/retrieval, and ticker detail/404 behavior. |

## Commands

Run from the repository root:

```powershell
python -m pytest Task1/artifacts/app/tests
docker compose -f Task1/artifacts/app/docker-compose.yml up --build
```

Open the website:

```text
http://127.0.0.1:5005/
```

Open API evidence:

```text
http://127.0.0.1:5005/health
http://127.0.0.1:5005/api/stocks
```

Check Docker status cleanly:

```powershell
docker compose -f Task1/artifacts/app/docker-compose.yml ps
```

## Manual Screenshot Steps

1. Commit and push the final approved code to GitHub.
2. For `01_commit_records.png`, open the GitHub repository, click the commit history, and capture meaningful commit records.
3. For `03_github_actions_success.png`, open the GitHub Actions tab, wait for the workflow to pass, open the successful run, and capture the green workflow result with pytest and Docker build steps if possible.
4. For `02_docker_deployed_website.png`, run the Docker deployment locally, open `http://127.0.0.1:5005/`, and capture the latest website in a normal browser window with the URL bar visible.
5. For optional API evidence, open `/health` or `/api/stocks` in the browser or terminal and capture readable JSON.
6. For optional Docker evidence, capture `docker compose ps` or a clean Docker Desktop container-running view.

## Current Local Verification

- Local pytest command passes with 9 tests; saved in `test_results/pytest_output.txt`.
- Local Flask endpoint and interaction checks pass for `/`, `/health`, `/api/stocks`, `/api/risk-summary`, `/api/watchlist`, `/api/feedback`, and `/api/stocks/<ticker>`; saved in `test_results/website_interaction_check.txt`.
- Docker and GitHub Actions evidence must remain real: if a screenshot cannot be captured directly, leave the filename pending and follow the manual steps above.
