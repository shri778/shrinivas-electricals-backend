from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(_name_)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    return jsonify({
        "response": f"You said: {user_message}"
    })
