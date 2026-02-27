from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

HF_API_KEY = os.environ.get("HF_API_KEY")

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


@app.route("/")
def home():
    return "Jiraiya AI with Hugging Face is Running 🚀"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"reply": "No message received"}), 400

        user_message = data["message"]

        payload = {
            "inputs": user_message,
            "parameters": {
                "max_new_tokens": 100,
                "temperature": 0.7
            }
        }

        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        result = response.json()

        print("HF Response:", result)

        if isinstance(result, list) and len(result) > 0:
            reply = result[0].get("generated_text", "No response generated.")
        elif isinstance(result, dict) and "error" in result:
            reply = "Model is loading. Please try again in 20 seconds."
        else:
            reply = "Unexpected model response."

        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": "Server error occurred"}), 500