# FinSight Builder Task1

Task1 contains the single coursework notebook and the generated artifacts for the FinSight Builder software component.

Notebook:
- `DTS114_FinSight_Builder.ipynb`

Generated artifacts:
- SDLC documentation in `artifacts/*.md` and `artifacts/user_stories.json`
- UML source in `artifacts/diagrams/*.puml`
- Flask app in `artifacts/app/flask`
- Tests in `artifacts/app/tests`
- Docker and CI files in `artifacts/app`

Run tests from the repository root:

```powershell
python -m pytest Task1/artifacts/app/tests
```

Run the Flask app:

```powershell
python Task1/artifacts/app/flask/main.py
```

Run with Docker Compose:

```powershell
docker compose -f Task1/artifacts/app/docker-compose.yml up --build
```

Boundary: this project uses sample educational stock data only. It does not provide stock prediction, trading advice, or investment recommendations.
