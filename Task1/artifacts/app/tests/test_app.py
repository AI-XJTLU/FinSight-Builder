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
    ok_response = client().get("/api/stocks/AAPL")
    missing_response = client().get("/api/stocks/UNKNOWN")
    assert ok_response.status_code == 200
    assert ok_response.get_json()["stock"]["ticker"] == "AAPL"
    assert missing_response.status_code == 404


def test_watchlist_validation_and_success():
    test_client = client()
    missing = test_client.post("/api/watchlist", json={})
    created = test_client.post("/api/watchlist", json={"ticker": "msft"})
    assert missing.status_code == 400
    assert created.status_code == 201
    assert "MSFT" in created.get_json()["watchlist"]


def test_feedback_validation_and_success():
    test_client = client()
    invalid = test_client.post("/api/feedback", json={"name": "Feiyu"})
    valid = test_client.post(
        "/api/feedback",
        json={"name": "Feiyu", "message": "Clear dashboard", "rating": 5},
    )
    assert invalid.status_code == 400
    assert valid.status_code == 201
    assert valid.get_json()["feedback"]["rating"] == 5


def test_risk_summary_shape():
    response = client().get("/api/risk-summary")
    assert response.status_code == 200
    assert set(response.get_json()["risk_summary"]) == {"low", "medium", "high"}


def test_index_page_and_generated_image_reference():
    response = client().get("/")
    assert response.status_code == 200
    html = response.get_data(as_text=True)
    assert "generated_market_banner.png" in html
    assert "API Evidence" in html


def test_generated_image_file_exists():
    image_path = APP_DIR / "static" / "generated_market_banner.png"
    assert image_path.exists()
    assert image_path.stat().st_size > 0


def test_feedback_get_returns_submitted_items():
    test_client = client()
    created = test_client.post(
        "/api/feedback",
        json={"name": "Feiyu", "message": "Useful risk summary", "rating": 4},
    )
    response = test_client.get("/api/feedback")
    assert created.status_code == 201
    assert response.status_code == 200
    data = response.get_json()
    assert data["count"] == 1
    assert data["items"][0]["message"] == "Useful risk summary"
