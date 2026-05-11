# FinSight Builder — Task1 Software Component

FinSight Builder is the Task1 software component for the DTS114TC AI Software Engineering coursework. It is an AI-assisted meta-software development project that generates and documents a small Flask API and single-page website for an educational stock watchlist and risk-briefing dashboard.

The system uses sample, fixed educational stock data only. It does **not** provide stock prediction, trading signals, buy/sell advice, portfolio optimisation, or investment recommendations.

## Coursework scope

Task1 contains the single required coursework notebook and all generated software artifacts.

Main notebook:

```text
Task1/DTS114_FinSight_Builder.ipynb
```

The notebook follows an AI-DLC-style workflow:

```text
Inception → Construction → Operation → Validation
```

It generates or records evidence for:

- SDLC documentation and requirements.
- UML diagrams.
- A functional Flask API.
- A single-page educational website.
- An automatically generated website image/banner.
- Pytest-based validation.
- Docker deployment support.
- CI/CD workflow evidence support.
- LLM / AI tooling evidence with human validation.

## Key generated artifacts

```text
Task1/
  DTS114_FinSight_Builder.ipynb
  README.md
  artifacts/
    problem_statement.md
    personas.md
    prd.md
    api_spec.md
    user_stories.json
    traceability_matrix.md
    generation_manifest.json
    references.md
    software_rubric_coverage.md
    llm_evidence/
      live_llm_generation_sample.md
    diagrams/
      use_case_diagram.puml
      use_case_diagram.png
      sequence_diagram.puml
      sequence_diagram.png
      finsight_builder_workflow.png
      render_status.json
    app/
      flask/
        main.py
        index.html
        requirements.txt
        static/generated_market_banner.png
      tests/test_app.py
      docker/Dockerfile
      docker-compose.yml
```

## Functional scope

The generated Flask app provides these endpoints:

```text
GET  /
GET  /health
GET  /api/stocks
GET  /api/stocks/<ticker>
GET  /api/watchlist
POST /api/watchlist
GET  /api/feedback
POST /api/feedback
GET  /api/risk-summary
```

The website displays:

- The generated FinSight Builder banner image.
- Sample stock educational briefing cards.
- A risk summary panel.
- API evidence links.
- A watchlist form.
- A feedback form.
- An educational-only / no-financial-advice disclaimer.

## Environment setup

Use the course-provided conda environment file from the coursework package:

```powershell
conda env create -f ai_in_se_cw.yml
conda activate ai_in_se_cw
```

If the environment already exists, activate it directly:

```powershell
conda activate ai_in_se_cw
```

Install Flask app dependencies if needed:

```powershell
pip install -r Task1/artifacts/app/flask/requirements.txt
```

## Run tests

From the repository root:

```powershell
python -m pytest Task1/artifacts/app/tests -q
```

Expected result:

```text
9 passed
```

## Run the Flask app locally

From the repository root:

```powershell
python Task1/artifacts/app/flask/main.py
```

Then open:

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
docker compose -f Task1/artifacts/app/docker-compose.yml up --build
```

Then open:

```text
http://127.0.0.1:5005/
```

To stop the container:

```powershell
docker compose -f Task1/artifacts/app/docker-compose.yml down
```

## LLM / AI tooling evidence

The project includes a safe LLM evidence pathway for DeepSeek when `DEEPSEEK_API_KEY` is available through an environment variable or `.env` file. API keys must never be printed, saved, or committed.

Relevant files:

```text
.env.example
Task1/artifacts/llm_evidence/live_llm_generation_sample.md
Task1/artifacts/generation_manifest.json
```

If live LLM generation is unavailable or a draft output fails validation, the notebook keeps a reviewed fallback/correction path so that the coursework remains reproducible.

## Evidence and validation files

The following files connect Task1 outputs to the marking criteria and Task2 evidence:

```text
Task1/artifacts/generation_manifest.json
Task1/artifacts/traceability_matrix.md
Task1/artifacts/software_rubric_coverage.md
Task1/artifacts/references.md
Task2/test_results/pytest_output.txt
Task2/test_results/website_interaction_check.txt
Task2/screenshots/
Task2/github_workflow_copy/ci.yml
Task2/clean_packaging_checklist.md
```

## Submission boundary

Final submission packaging should be handled from the repository root and should include only:

```text
2472811-Feiyu_Chen/
  Task1/
  Task2/
```

The final zip should exclude development-only files such as:

```text
.git/
.github/
.pytest_cache/
__pycache__/
.ipynb_checkpoints/
*.pyc
*.zip
.env
private keys
temporary logs
.flask_pid
```

See:

```text
Task2/clean_packaging_checklist.md
```

## Academic and financial boundary

This software component demonstrates AI-assisted software engineering practice. The generated web app is for educational demonstration only. It uses fixed sample data and must not be interpreted as financial advice, trading advice, or investment recommendation.
