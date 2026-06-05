# Task 2 Deployment Notes

This document records the deployment evidence for the FinSight Builder CW-Software-Component.

## 1. Local Docker deployment

The generated Flask application was first deployed locally with Docker Compose.

Docker Compose file:

`Task1/artifacts/app/docker/docker-compose.yml`

The local Docker deployment exposed the application on:

`http://127.0.0.1:5005/`

The local deployment evidence includes:

- website homepage screenshot;
- API endpoint screenshot;
- Docker container running screenshot;
- supporting command outputs in `test_results/`.

This local deployment checked that the generated Flask app, dependencies, static banner image, API routes and port configuration could run in a repeatable containerised environment.

## 2. Cloud deployment on Render

The deployment stage was also completed on Render as a cloud platform.

Render service URL:

`https://finsight-builder.onrender.com`

Render was configured from the organisation GitHub repository:

`AI-XJTLU/FinSight-Builder`

Deployment settings:

- Branch: `main`
- Root Directory: `Task1/artifacts/app/flask`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn main:app --bind 0.0.0.0:$PORT`
- Runtime: Python 3
- Plan: Free

The cloud deployment was checked through:

- `https://finsight-builder.onrender.com/`
- `https://finsight-builder.onrender.com/health`
- `https://finsight-builder.onrender.com/api/stocks`

The Render evidence shows that the Flask dashboard can run outside the local machine on a cloud-hosted service.

## 3. CI/CD evidence

GitHub Actions was used to run automated validation after commits. The workflow installs the Flask app dependencies, runs pytest tests, and checks the application build process.

The workflow copy is stored at:

`Task2/github_workflow_copy/ci.yml`

The GitHub Actions success screenshot is stored in:

`Task2/screenshots/03_github_actions_success.png`
