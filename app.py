from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

HF_TOKEN = os.environ.get("HF_TOKEN")

@app.route("/test")
def test():
    return "Chat route exists"

@app.route("/")
def home():
    return "Backend is running "
    
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")

    response = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-small",
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": user_input}
    )

    return jsonify(response.json())
if __name__ == "__main__":
    port = int(os.environ.get("PORT",
10000))
    app.run(host+"0.0.0.0", port=port
