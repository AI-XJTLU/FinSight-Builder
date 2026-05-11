# Product Requirements Document

## Overview
FinSight Builder is an AI-powered meta-software development notebook that generates a Flask API and website for a sample stock watchlist and educational risk briefing dashboard. The notebook itself is the main software engineering artifact: it demonstrates how prompts, LLM/fallback generation, human validation, UML, implementation, tests, CI/CD, Docker, and evidence collection connect.

## Functional requirements
- FR-001: Generate and save a problem statement, personas, PRD, user stories, and API specification.
- FR-002: Generate and save PlantUML source and PNG UML evidence.
- FR-003: Provide a Flask API with `/health`, `/api/stocks`, `/api/stocks/<ticker>`, `/api/watchlist`, `/api/feedback`, `/api/risk-summary`, and `/`.
- FR-004: Provide a website that displays stock cards, risk summary, generated banner image, watchlist form, feedback form, and disclaimer.
- FR-005: Generate pytest tests for success and validation/error paths.
- FR-006: Generate Dockerfile, Docker Compose, and GitHub Actions workflow files.

## Non-functional requirements
- NFR-001: The notebook must rerun without exposing API keys.
- NFR-002: The generated Flask application must run locally and in Docker on port 5005.
- NFR-003: The project must avoid financial advice, prediction, and trading automation.
- NFR-004: The final software package must contain a clean Task1/Task2 structure.

## Constraints and assumptions
- Uses fixed educational sample stock data.
- LLM generation is preferred when credentials are available; reviewed fallback keeps the notebook reproducible.
- External image and PlantUML rendering services are optional, not required for successful reruns.

## Risks
- R1: API key or network unavailable; mitigation: reviewed fallback outputs and local image fallback.
- R2: PlantUML renderer unavailable; mitigation: local rendering attempts followed by explicit fallback status.
- R3: Submission zip pollution; mitigation: clean packaging checklist.

## Acceptance criteria
- AC-001: Task1 contains exactly one notebook.
- AC-002: Required generated artifacts exist under Task1/artifacts.
- AC-003: `python -m pytest Task1/artifacts/app/tests` passes.
- AC-004: Docker and GitHub Actions files exist and include pytest plus Docker build workflow.
- AC-005: Task2 evidence requirements are listed and missing evidence is clearly identified.
