from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    print("DEBUG: Received data =", data)  # temporary debug

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_message = data["message"]
    reply = "You said: " + user_message

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
