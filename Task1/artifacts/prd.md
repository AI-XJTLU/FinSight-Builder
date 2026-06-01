# Product Requirements Document

## Overview
- FinSight Club Dashboard is a Flask API and website for weekly university finance club discussions.
- The product presents fixed sample stocks, educational risk briefings, risk category summaries, and feedback collection.

## Goals
- Help students prepare for discussion with a small educational stock watchlist.
- Explain low, medium, and high risk categories in plain English.
- Let organisers collect feedback after each session.

## Non-Goals
- The product is not a live market-data platform.
- The product does not provide financial advice or real-money decision support.
- The product does not require accounts or a persistent database.

## User Personas
- Beginner Student Investor: needs approachable explanations and visible risk labels.
- Finance Club Member: needs a focused watchlist and short risk context.
- Club Organiser: needs feedback collection and predictable session materials.
- Finance Workshop Facilitator: needs a teaching aid with clear educational boundaries.

## Key Features
- Stock briefing cards with ticker, company name, sector, mock price, risk level, and briefing.
- Watchlist form for supported tickers.
- Risk summary grouped by low, medium, and high categories.
- Feedback form with rating validation.

## User Flows
- A student opens the dashboard, reviews stock cards, and reads the risk summary.
- A member adds a supported ticker to the watchlist.
- An organiser collects feedback after the session.

## Functional Requirements
- Serve the dashboard at `/` and JSON health data at `/health`.
- Return stock list and single-ticker briefing data through API endpoints.
- Validate watchlist and feedback submissions.
- Display the generated market education banner and required disclaimer.

## Non-Functional Requirements
- Keep the interface responsive and readable for beginner users.
- Use fixed sample data for reproducible demonstrations.
- Return clear JSON errors for invalid input.

## Constraints/Assumptions
- Stock prices are mock values used only for education.
- Watchlist and feedback can be stored in memory for the lightweight version.
- The application should run locally with simple Python dependencies.

## Success Metrics
- Users can load the dashboard and see the generated image.
- Users can add a supported ticker and submit valid feedback.
- Invalid inputs return understandable errors.

## Open Questions
- Which sample stocks should the finance club prefer for future sessions?
