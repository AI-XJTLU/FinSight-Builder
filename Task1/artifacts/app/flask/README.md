# Flask Feedback API + HTML Frontend

An integrated Flask app that provides a simple **Feedback API** and an **interactive HTML frontend** in one server. Submit feedback via REST endpoints or use the browser UI—**the HTML frontend is served automatically** by Flask.

## Setup

```bash
pip install flask flask-cors
```

## Run

```bash
python main.py
```

## Access

Open the app in your browser:

- http://127.0.0.1:5005

The interactive HTML page loads from the same server and lets you submit/view feedback without extra setup.

## API Usage

### Submit feedback (POST `/feedback`)

```bash
curl -X POST http://127.0.0.1:5005/feedback \
  -H "Content-Type: application/json" \
  -d '{"name":"Alex","message":"Great app!","rating":5}'
```

### Retrieve feedback (GET `/feedback`)

```bash
curl http://127.0.0.1:5005/feedback
```