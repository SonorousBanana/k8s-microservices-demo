from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)

# Fake data
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
    {"id": 3, "name": "Charlie", "email": "charlie@example.com"}
]

metrics = ["cpu", "memory", "disk"]

@app.route("/health")
def health():
    return jsonify(status="ok", timestamp=datetime.utcnow().isoformat())

@app.route("/api/users")
def get_users():
    return jsonify(users=users)

@app.route("/api/metrics")
def get_metrics():
    data = []
    for m in metrics:
        data.append({
            "metric": m,
            "value": round(random.uniform(10, 100), 2),
            "timestamp": datetime.utcnow().isoformat()
        })
    return jsonify(metrics=data)

@app.route("/api/user/<int:user_id>")
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify(error="User not found"), 404

@app.route("/api/greet", methods=["POST"])
def greet_user():
    payload = request.json
    name = payload.get("name", "Guest")
    return jsonify(message=f"Hello, {name}!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

