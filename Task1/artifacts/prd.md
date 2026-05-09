# Product Requirements Document

## Overview
FinSight Builder is an AI-powered meta-software development notebook that generates a Flask API and website for a stock watchlist and educational risk briefing dashboard.

## Goals
- Demonstrate an AI-DLC workflow from inception through construction and operation.
- Generate documentation, UML, Flask code, website code, image asset, tests, Docker files, and CI workflow evidence.
- Provide educational sample stock risk summaries with an explicit non-advice disclaimer.

## Non-Goals
- Stock price prediction.
- Buy, sell, hold, or portfolio allocation recommendations.
- Live trading or mandatory live financial API integration.

## Functional Requirements
- Show a stock dashboard with ticker, company name, mock price, sector, risk level, and risk briefing.
- Allow users to add supported tickers to an in-memory watchlist.
- Provide health, stock list, stock detail, watchlist, feedback, and risk-summary API endpoints.
- Display an automatically generated market banner image on the website.
- Validate feedback and invalid watchlist submissions.

## Non-Functional Requirements
- Runs locally with Flask and through Docker Compose.
- Tests can be executed with pytest.
- CI workflow runs tests and a Docker build check.
- All pages and API responses maintain an educational disclaimer.

## Success Metrics
- Core API tests pass locally and in CI.
- Docker deployment serves the website and JSON endpoints on port 5005.
- Submission package contains Task1 notebook/artifacts and Task2 evidence.
