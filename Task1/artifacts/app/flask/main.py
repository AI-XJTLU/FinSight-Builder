from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__, static_folder="static")

DISCLAIMER = "For educational demonstration only. Not financial advice."

STOCKS = [
    {"ticker": "AAPL", "name": "Apple Inc.", "sector": "Technology hardware", "mock_price": 184.35, "risk_level": "medium", "briefing": "Device cycles, services growth, supply chain resilience, and consumer demand can affect discussion risk."},
    {"ticker": "MSFT", "name": "Microsoft Corporation", "sector": "Cloud and productivity software", "mock_price": 421.16, "risk_level": "low", "briefing": "Diversified software and cloud revenue may reduce volatility, while infrastructure spending remains important."},
    {"ticker": "NVDA", "name": "NVIDIA Corporation", "sector": "Semiconductors", "mock_price": 912.44, "risk_level": "high", "briefing": "AI chip demand, valuation, export controls, and supply capacity create a wider range of discussion risks."},
    {"ticker": "TSLA", "name": "Tesla, Inc.", "sector": "Electric vehicles", "mock_price": 177.53, "risk_level": "high", "briefing": "Margins, delivery growth, battery costs, regulation, and leadership attention can influence uncertainty."},
]

watchlist = []
feedback_items = []


def find_stock(ticker):
    normalized = str(ticker or "").strip().upper()
    return next((stock for stock in STOCKS if stock["ticker"] == normalized), None)


@app.get("/health")
def health():
    return jsonify(status="ok", service="FinSight Club Dashboard", disclaimer=DISCLAIMER)


@app.get("/api/stocks")
def list_stocks():
    return jsonify(stocks=STOCKS, count=len(STOCKS), disclaimer=DISCLAIMER)


@app.get("/api/stocks/<ticker>")
def stock_detail(ticker):
    stock = find_stock(ticker)
    if stock is None:
        return jsonify(error="stock_not_found", disclaimer=DISCLAIMER), 404
    return jsonify(stock=stock, disclaimer=DISCLAIMER)


@app.post("/api/watchlist")
def add_watchlist_item():
    payload = request.get_json(silent=True) or {}
    ticker = str(payload.get("ticker", "")).strip().upper()
    if not ticker:
        return jsonify(error="ticker is required", disclaimer=DISCLAIMER), 400
    stock = find_stock(ticker)
    if stock is None:
        return jsonify(error="ticker is not in the educational sample dataset", disclaimer=DISCLAIMER), 404
    if ticker not in watchlist:
        watchlist.append(ticker)
    return jsonify(message="ticker added", watchlist=watchlist, stock=stock, disclaimer=DISCLAIMER), 201


@app.get("/api/watchlist")
def get_watchlist():
    items = [stock for stock in STOCKS if stock["ticker"] in watchlist]
    return jsonify(watchlist=items, tickers=watchlist, disclaimer=DISCLAIMER)


@app.get("/api/risk-summary")
def risk_summary():
    counts = {"low": 0, "medium": 0, "high": 0}
    for stock in STOCKS:
        counts[stock["risk_level"]] += 1
    return jsonify(risk_summary=counts, disclaimer=DISCLAIMER)


@app.post("/api/feedback")
def submit_feedback():
    payload = request.get_json(silent=True) or {}
    name = str(payload.get("name", "")).strip()
    message = str(payload.get("message", "")).strip()
    rating = payload.get("rating")
    if not name or not message or rating is None:
        return jsonify(error="name, message, and rating are required"), 400
    try:
        rating = int(rating)
    except (TypeError, ValueError):
        return jsonify(error="rating must be an integer"), 400
    if rating < 1 or rating > 5:
        return jsonify(error="rating must be between 1 and 5"), 400
    item = {"id": len(feedback_items) + 1, "name": name, "message": message, "rating": rating}
    feedback_items.append(item)
    return jsonify(message="feedback submitted", feedback=item), 201


@app.get("/api/feedback")
def list_feedback():
    return jsonify(items=feedback_items, count=len(feedback_items))


@app.get("/")
def index():
    return send_from_directory(".", "index.html")


@app.get("/stock/<ticker>")
def stock_detail_page(ticker):
    return send_from_directory(".", "stock_detail.html")


@app.get("/<path:filename>")
def serve_static_file(filename):
    return send_from_directory(".", filename)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5005, debug=False)
