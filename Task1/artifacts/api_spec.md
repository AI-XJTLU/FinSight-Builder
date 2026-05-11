# API Specification

Base URL: `http://127.0.0.1:5005`

| Endpoint | Method | Story IDs | Test case | Purpose | Validation / response notes |
|---|---|---|---|---|---|
| `/` | GET | US-001 | `test_index_page_and_generated_image_reference` | Serve generated dashboard website | Returns 200 and references `static/generated_market_banner.png`. |
| `/health` | GET | US-005 | `test_health_endpoint` | Deployment health check | Returns service status and disclaimer. |
| `/api/stocks` | GET | US-001 | `test_stocks_have_required_fields` | Return educational sample stock list | Includes ticker, name, sector, mock_price, risk_level, and briefing. |
| `/api/stocks/<ticker>` | GET | US-002 | `test_stock_detail_and_unknown_ticker` | Return one educational stock briefing | Known ticker returns 200; unknown ticker returns 404. |
| `/api/watchlist` | GET | US-003 | covered by watchlist integration path | Return in-memory watchlist | Returns selected sample stocks and ticker list. |
| `/api/watchlist` | POST | US-003 | `test_watchlist_validation_and_success` | Add supported ticker to watchlist | Missing ticker returns 400; unsupported ticker returns 404; valid ticker returns 201. |
| `/api/feedback` | GET | US-004 | `test_feedback_get_returns_submitted_items` | Return submitted feedback items | Returns list and count after POST. |
| `/api/feedback` | POST | US-004 | `test_feedback_validation_and_success` | Submit feedback | Requires name, message, and rating; rating must be 1-5. |
| `/api/risk-summary` | GET | US-001/US-005 | `test_risk_summary_shape` | Return counts by risk level | Returns low, medium, and high keys. |

All financial content is fixed educational sample data only. The API does not provide investment recommendations, predictions, trading automation, or financial advice.
