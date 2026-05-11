# Live LLM Generation Evidence

## Status
Live LLM generation was unavailable in this local run or the draft did not pass validation; this reviewed correction is saved for reproducible assessment.

When `DEEPSEEK_API_KEY` is provided through `.env` or the process environment, the notebook attempts a DeepSeek `deepseek-chat` call. The output is saved only if it describes implemented project artifacts and avoids invented endpoints, libraries, diagrams, screenshots, or deployment evidence.

## Actual Implemented Evidence

### SDLC documentation
- `Task1/artifacts/problem_statement.md`
- `Task1/artifacts/personas.md`
- `Task1/artifacts/prd.md`
- `Task1/artifacts/user_stories.json`
- `Task1/artifacts/api_spec.md`
- `Task1/artifacts/traceability_matrix.md`
- `Task1/artifacts/generation_manifest.json`

### UML diagrams
- `Task1/artifacts/diagrams/use_case_diagram.puml`
- `Task1/artifacts/diagrams/use_case_diagram.png`
- `Task1/artifacts/diagrams/sequence_diagram.puml`
- `Task1/artifacts/diagrams/sequence_diagram.png`

### Flask API endpoints
- `GET /`
- `GET /health`
- `GET /api/stocks`
- `GET /api/stocks/<ticker>`
- `GET/POST /api/watchlist`
- `GET/POST /api/feedback`
- `GET /api/risk-summary`

### Website evidence
- `Task1/artifacts/app/flask/index.html`
- `Task1/artifacts/app/flask/static/generated_market_banner.png`
- Stock cards populated from `/api/stocks`
- Risk summary populated from `/api/risk-summary`
- Watchlist form, feedback form, educational disclaimer, and API evidence section

### Testing, deployment and CI evidence
- 9 pytest tests in `Task1/artifacts/app/tests/test_app.py`
- `Task1/artifacts/app/docker/Dockerfile`
- `Task1/artifacts/app/docker-compose.yml`
- `.github/workflows/ci.yml`
- Task2 screenshot and command-output evidence

## Boundary
The generated application uses fixed educational sample data only. It does not provide stock prediction, trading signals, buy/sell advice, investment recommendations, portfolio optimisation, or financial advice.
