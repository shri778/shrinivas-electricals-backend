from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Hugging Face API settings
API_URL = "https://api-inference.huggingface.co/models/gpt2"
HF_API_KEY = os.getenv("HF_API_KEY")

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_message = data["message"]

      response = requests.post(
            API_URL,
            headers=headers,
            json={"inputs": user_message},
            timeout=30
        )

        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            reply = result[0]["generated_text"]
        else:
            reply = str(result)

    except Exception as e:
        reply = "Error: " + str(e)

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
