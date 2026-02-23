from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

HF_TOKEN = os.environ.get("HF_TOKEN")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    response = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-small",
        headers={"Authorization": f"Bearer {HF_TOKEN}"},
        json={"inputs": user_input}
    )

    return jsonify(response.json())
