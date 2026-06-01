# FinSight Builder - Task1

FinSight Builder is the generator notebook for Task1. It follows an AI-DLC practical workflow to generate documentation, UML, Flask code, website code, an image asset, tests, Docker files, and a CI workflow file.

The generated application is FinSight Club Dashboard, a Flask API and website for a university finance club's educational stock watchlist, risk briefings, risk summary, and session feedback.

## Main Notebook

```text
Task1/DTS114_FinSight_Builder.ipynb
```

Task1 should contain only this one notebook. Supporting generated files are stored under `Task1/artifacts/`.

## Generated Product Files

```text
Task1/artifacts/
  problem_statement.md
  personas.md
  prd.md
  user_stories.json
  api_spec.md
  references.md
  diagrams/
    use_case_diagram.puml
    use_case_diagram.png
    sequence_diagram.puml
    sequence_diagram.png
  app/
    flask/
      main.py
      index.html
      stock_detail.html
      requirements.txt
      static/generated_market_banner.png
    tests/test_app.py
    docker/Dockerfile
    docker/docker-compose.yml
```

## Run Tests

From the repository root:

```powershell
python -m pytest Task1/artifacts/app/tests -q
```

## Run the Flask App

From the repository root:

```powershell
python Task1/artifacts/app/flask/main.py
```

Open:

```text
http://127.0.0.1:5005/
```

Useful API checks:

```text
http://127.0.0.1:5005/health
http://127.0.0.1:5005/api/stocks
http://127.0.0.1:5005/api/risk-summary
```

## Run with Docker Compose

From the repository root:

```powershell
docker compose -f Task1/artifacts/app/docker/docker-compose.yml up --build
```

To stop:

```powershell
docker compose -f Task1/artifacts/app/docker/docker-compose.yml down
```

## Boundary

The generated application uses fixed sample data and displays:

```text
For educational demonstration only. Not financial advice.
```

Real API keys must be supplied through environment variables or a local `.env` file and must not be printed or committed.

## Source Transparency

Implementation sources are cited in `Task1/artifacts/references.md`. The notebook uses the teacher-provided baseline utilities and records the official Flask, pytest, Docker, GitHub Actions, and PlantUML documentation used during implementation.
