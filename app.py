
from flask import Flask, jsonify, request

app = Flask(__name__)

# Temporary task storage
tasks = [
    {"id": 1, "title": "Learn Python", "completed": False},
    {"id": 2, "title": "Learn Flask", "completed": False}
]

# Homepage
@app.route("/")
def home():
    return jsonify({"message": "Welcome to DevTracker API!"})

# Get all tasks
@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    return jsonify(tasks)

# Add a new task
@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    if not data or not data.get("title", "").strip():
        return jsonify({"error": "Task title is required"}), 400

    new_task = {
        "id": max([task["id"] for task in tasks], default=0) + 1,
        "title": data["title"].strip(),
        "completed": False
    }

    tasks.append(new_task)

    return jsonify(new_task), 201

if __name__ == "__main__":
    app.run(debug=True)
