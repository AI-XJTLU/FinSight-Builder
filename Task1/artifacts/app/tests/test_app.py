import sys
from pathlib import Path

APP_DIR = Path(__file__).resolve().parents[1] / "flask"
sys.path.insert(0, str(APP_DIR))

from main import app, feedback_items, watchlist  # noqa: E402


def client():
    app.config.update(TESTING=True)
    watchlist.clear()
    feedback_items.clear()
    return app.test_client()


def test_health_endpoint():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_stocks_have_required_fields():
    response = client().get("/api/stocks")
    data = response.get_json()
    assert response.status_code == 200
    assert data["count"] >= 3
    for stock in data["stocks"]:
        assert {"ticker", "name", "mock_price", "risk_level", "briefing"} <= stock.keys()


def test_stock_detail_and_unknown_ticker():
    assert client().get("/api/stocks/AAPL").status_code == 200
    assert client().get("/api/stocks/UNKNOWN").status_code == 404


def test_stock_detail_page_supports_client_side_api_fetch():
    response = client().get("/stock/AAPL")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "/api/stocks/" in html
    assert "Back to dashboard" in html
    assert "Stock not found" in html


def test_index_page_has_stock_detail_navigation():
    response = client().get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "View details" in html
    assert 'href="/stock/${encodeURIComponent(stock.ticker)}"' in html


def test_watchlist_validation_and_success():
    test_client = client()
    assert test_client.post("/api/watchlist", json={}).status_code == 400
    assert test_client.post("/api/watchlist", json={"ticker": "ZZZZ"}).status_code == 404
    created = test_client.post("/api/watchlist", json={"ticker": "msft"})
    assert created.status_code == 201
    assert "MSFT" in created.get_json()["watchlist"]


def test_feedback_validation_and_success():
    test_client = client()
    assert test_client.post("/api/feedback", json={"name": "Feiyu"}).status_code == 400
    assert test_client.post("/api/feedback", json={"name": "Feiyu", "message": "Clear", "rating": 6}).status_code == 400
    valid = test_client.post("/api/feedback", json={"name": "Feiyu", "message": "Clear dashboard", "rating": 5})
    assert valid.status_code == 201
    assert valid.get_json()["feedback"]["rating"] == 5


def test_risk_summary_shape():
    response = client().get("/api/risk-summary")
    assert response.status_code == 200
    assert set(response.get_json()["risk_summary"]) == {"low", "medium", "high"}


def test_index_page_and_generated_image_reference():
    response = client().get("/")
    html = response.get_data(as_text=True)
    assert response.status_code == 200
    assert "generated_market_banner.png" in html
    assert "For educational demonstration only. Not financial advice." in html


def test_generated_image_file_exists():
    image_path = APP_DIR / "static" / "generated_market_banner.png"
    assert image_path.exists()
    assert image_path.stat().st_size > 0


def test_feedback_get_returns_submitted_items():
    test_client = client()
    assert test_client.post("/api/feedback", json={"name": "Feiyu", "message": "Useful risk summary", "rating": 4}).status_code == 201
    response = test_client.get("/api/feedback")
    assert response.status_code == 200
    assert response.get_json()["count"] == 1
