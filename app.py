from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import requests

app = Flask(__name__)
CORS(app)

# Hugging Face API Key
HF_API_KEY = os.environ.get("HF_API_KEY")
HF_MODEL = "gpt2"  # or your preferred Hugging Face model

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

@app.route("/")
def home():
    return "Backend is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    print("DEBUG: Received data =", data)

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_message = data["message"]

    try:
        payload = {
            "inputs": user_message
        }
        response = requests.post(
            f"https://api-inference.huggingface.co/models/{HF_MODEL}",
            headers=headers,
            json=payload,
            timeout=30
        )
        result = response.json()

        # Hugging Face text models usually return [{'generated_text': '...'}]
        if isinstance(result, list) and "generated_text" in result[0]:
            reply = result[0]["generated_text"]
        elif isinstance(result, dict) and "error" in result:
            reply = "Model error: " + result["error"]
        else:
            reply = str(result)

    except Exception as e:
        print("Hugging Face API Error:", e)
        reply = "Sorry, I couldn't process your message."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
