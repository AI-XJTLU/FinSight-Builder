# Software Component Coverage Matrix

| Marking criterion | Evidence in this submission |
|---|---|
| Generate documentation | Notebook writes `problem_statement.md`, `personas.md`, `prd.md`, `user_stories.json`, and `api_spec.md`. |
| Prompt a website with generated image | Notebook writes `index.html` and generates `static/generated_market_banner.png`; Task2 includes website screenshot. |
| Coherent professional notebook | Notebook follows baseline AI-DLC phases: setup, Inception, Construction, Operation, validation. |
| UML diagrams | Notebook writes PlantUML sources and PNG diagram evidence for use case and sequence views. |
| AI-specific tooling | Prompt templates, baseline `utils.py`, optional API-key checks, deterministic fallback generation, and human-reviewed outputs are documented. |
| Version control | Git repository uses `main` and remote `origin`; Task2 reserves commit-history screenshot evidence. |
| Workflow | `.github/workflows/ci.yml` runs pytest and Docker image build. |
| Testing | `Task1/artifacts/app/tests/test_app.py` covers API success and validation/error paths. |
| Deployment | Dockerfile and Compose deploy the Flask API/website on port 5005; Task2 contains website/API/container evidence. |
