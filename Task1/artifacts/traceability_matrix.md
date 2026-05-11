# Traceability Matrix

| User Story ID | Requirement | API Endpoint | Test Case | Evidence File |
|---|---|---|---|---|
| US-001 | FR-004 | `/ and /api/stocks` | `test_index_page_and_generated_image_reference; test_stocks_have_required_fields` | `Task1/artifacts/app/tests/test_app.py` |
| US-002 | FR-003 | `/api/stocks/<ticker>` | `test_stock_detail_and_unknown_ticker` | `Task1/artifacts/app/tests/test_app.py` |
| US-003 | FR-003 | `/api/watchlist` | `test_watchlist_validation_and_success` | `Task1/artifacts/app/tests/test_app.py` |
| US-004 | FR-003 | `/api/feedback` | `test_feedback_validation_and_success; test_feedback_get_returns_submitted_items` | `Task1/artifacts/app/tests/test_app.py` |
| US-005 | FR-005/FR-006 | `N/A` | `test_risk_summary_shape plus CI pytest command` | `Task1/artifacts/app/tests/test_app.py` |
