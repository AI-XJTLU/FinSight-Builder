# API Specification

Application: FinSight Club Dashboard
Base URL: http://127.0.0.1:5005
Disclaimer: For educational demonstration only. Not financial advice.

## Website Routes
- `GET /`: serves the English website interface with the generated market education banner, sample stock cards, watchlist form, feedback form, and visible disclaimer.
- `GET /stock/<ticker>`: serves the stock detail page, which loads the supported ticker briefing from `GET /api/stocks/<ticker>`.

## GET /health
Returns service health information.

Example response:
```json
{"status": "ok", "service": "FinSight Club Dashboard", "disclaimer": "For educational demonstration only. Not financial advice."}
```

## GET /api/stocks
Returns the fixed educational sample stock list.

Response fields include ticker, name, sector, mock_price, risk_level, and briefing.

## GET /api/stocks/<ticker>
Returns one stock briefing for a supported ticker. Unknown tickers return 404 with `stock_not_found`.

## POST /api/watchlist
Adds a supported ticker to the in-memory watchlist.

Request body:
```json
{"ticker": "AAPL"}
```
Validation:
- Missing ticker returns 400.
- Unsupported ticker returns 404.

## GET /api/watchlist
Returns the current in-memory watchlist as both ticker symbols and stock objects.

## GET /api/risk-summary
Returns counts for low, medium, and high risk categories.

## POST /api/feedback
Accepts post-session feedback.

Request body:
```json
{"name": "Student", "message": "Useful discussion", "rating": 5}
```
Validation:
- name, message, and rating are required.
- rating must be an integer from 1 to 5.

## GET /api/feedback
Returns submitted feedback items and a count.

## Boundary
The API returns educational sample data only. It does not provide prediction, trading advice, buy/sell recommendations, portfolio optimisation, investment recommendations, or real-money decision support.
