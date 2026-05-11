# Personas

## Student Developer
- Goals: build a reproducible AI software engineering notebook, show how prompts become artifacts, and produce runnable Flask/Docker/CI evidence.
- Frustrations: opaque generated code, static documentation that does not connect to tests, and deployment evidence that is hard to reproduce.
- Success criteria: every generated artifact has a source, validation checks, output path, and next-phase purpose; tests pass locally; Docker and CI files are present.
- Linked requirements: documentation generation, UML generation, Flask implementation, pytest, Docker, CI workflow, Task2 evidence.

## Learner User
- Goals: open a simple dashboard, review sample stock risk briefings, add supported tickers to a watchlist, and submit feedback.
- Frustrations: confusing finance dashboards, hidden assumptions, and advice-like wording.
- Success criteria: visible non-advice disclaimer, clear sample data, validation feedback for unsupported tickers, and readable risk summaries.
- Linked requirements: website home page, `/api/stocks`, `/api/stocks/<ticker>`, `/api/watchlist`, `/api/feedback`, `/api/risk-summary`.

## Coursework Marker
- Goals: evaluate whether the project demonstrates AI-specific tooling, SDLC structure, UML, testing, workflow, version control, and deployment.
- Frustrations: notebooks that only paste final outputs, missing traceability, missing screenshots, or generated files that cannot be rerun.
- Success criteria: notebook follows a visible AI-DLC chain, generated artifacts are saved, tests pass, CI/Docker configuration exists, and Task2 evidence is named clearly.
- Linked requirements: generation manifest, traceability matrix, rubric coverage matrix, screenshots, test output, and clean packaging checklist.
