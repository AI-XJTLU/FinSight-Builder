from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
feedback_db = []

@app.get("/health")
def health():
    return jsonify(status="ok")
# Endpoint for Story 1: Player
@app.route("/api/tictactoe/info", methods=["GET"])
def tictactoe_info():
    return jsonify({
        "game": "Tic-Tac-Toe",
        "rules": "Two players alternate placing X/O on a 3x3 grid. First to 3 in a row wins; otherwise it's a draw.",
        "how_to_launch": {"method": "POST", "path": "/api/tictactoe/launch"},
        "feedback": {"method": "POST", "path": "/api/tictactoe/feedback", "body": {"message": "string"}}
    }), 200

@app.route("/api/tictactoe/launch", methods=["POST"])
def tictactoe_launch():
    game_id = str(len(feedback_db) + 1)
    session = {"type": "tictactoe_session", "game_id": game_id, "board": [""] * 9, "turn": "X", "status": "in_progress"}
    feedback_db.append(session)
    return jsonify({"message": "Game launched", "session": session}), 201

# Endpoint for Story 2: Player
@app.route("/feedback", methods=["POST"])
def submit_feedback():
    data = request.get_json(silent=True) or {}
    
    # Extract fields from request
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")
    rating = data.get("rating")
    
    # Validate required fields
    if not name or not email or not message or rating is None:
        return jsonify(error="name, email, message, and rating are required"), 400
    
    # Validate rating
    try:
        rating = int(rating)
    except (TypeError, ValueError):
        return jsonify(error="rating must be an integer"), 400
    
    if rating < 1 or rating > 5:
        return jsonify(error="rating must be between 1 and 5"), 400
    
    # Create feedback item
    item = {
        "id": len(feedback_db) + 1,
        "name": str(name),
        "email": str(email),
        "message": str(message),
        "rating": rating
    }
    
    feedback_db.append(item)
    return jsonify({"message": "Feedback submitted successfully", "feedback": item}), 201

@app.route("/feedback", methods=["GET"])
def list_feedback():
    return jsonify(items=feedback_db, count=len(feedback_db)), 200

# Endpoint for Story 3: Product Manager
@app.route("/feedback/triage", methods=["GET"])
def list_new_feedback():
    new_items = [f for f in feedback_db if f.get("status", "new") == "new"]
    return jsonify({"count": len(new_items), "items": new_items}), 200

@app.route("/feedback/<int:fid>/triage", methods=["PATCH"])
def triage_feedback(fid):
    data = request.get_json(silent=True) or {}
    item = next((f for f in feedback_db if f.get("id") == fid), None)
    if not item: return jsonify({"error": "not_found"}), 404
    for k in ("status", "assignee"): 
        if k in data: item[k] = data[k]
    if "tags" in data:
        tags = data["tags"]
        if not isinstance(tags, list): return jsonify({"error": "tags_must_be_list"}), 400
        item["tags"] = tags
    item.setdefault("status", "new"); item.setdefault("tags", []); item.setdefault("assignee", None)
    return jsonify({"item": item}), 200
# Serve frontend
@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)


if __name__ == '__main__':
    # Bind to 0.0.0.0 to make it accessible from Docker
    app.run(host='0.0.0.0', debug=True, port=5005)