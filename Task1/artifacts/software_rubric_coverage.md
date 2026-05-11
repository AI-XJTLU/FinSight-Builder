# Software Component Coverage Matrix

| Marking criterion | Evidence in this submission |
|---|---|
| Generate documentation | Each Inception artifact is produced by prompt -> `get_completion(...)` when available -> `clean_llm_output(...)` -> validation -> reviewed fallback if needed; outputs are saved to `problem_statement.md`, `personas.md`, `prd.md`, `user_stories.json`, and `api_spec.md`. |
| Prompt a website with generated image | Notebook writes `index.html` from the PRD/API spec and generates `static/generated_market_banner.png`; Task2 includes website screenshot instructions and evidence. |
| Coherent professional notebook | Notebook uses AI-DLC sections, artifact dependency mapping, manifest evidence, traceability, validation summaries, and clean output paths. |
| UML diagrams | Notebook saves PlantUML source, attempts local PlantUML, records render method in `render_status.json`, and uses a professional deterministic fallback only when PlantUML is unavailable. |
| AI-specific tooling | Uses `load_environment`, `setup_llm_client`, `get_completion`, `clean_llm_output`, a safe DeepSeek live-generation path, optional image API narrative, deterministic fallbacks, and human-reviewed validation. |
| Version control | Git repository uses `main` and remote `origin`; Task2 defines mandatory real GitHub commit-history evidence. |
| Workflow | `.github/workflows/ci.yml` runs pytest and Docker image build; Task2 defines mandatory real GitHub Actions success evidence. |
| Testing | `Task1/artifacts/app/tests/test_app.py` contains 9 pytest tests covering API success, validation/error paths, website image reference, and feedback retrieval. |
| Deployment | Dockerfile and Compose deploy the Flask API/website on port 5005; Task2 contains or requests real website/API/container evidence. |
