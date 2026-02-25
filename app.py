from flask import Flask, request,
jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "GET":
        return "Chat route is working"

    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_message = data["message"]
    reply = "You said: " + user_message

    return jsonify({"reply": reply})
    user_message = request.json["message"]

    reply = "You said: " + user_message

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
