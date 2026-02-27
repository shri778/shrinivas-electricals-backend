from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Hugging Face settings
HF_API_KEY = os.environ.get("HF_API_KEY")
API_URL = "https://router.huggingface.co/hf-inference/models/gpt2"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}


@app.route("/")
def home():
    return "Backend is running"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"reply": "No message received"}), 400

        user_message = data["message"]

        payload = {
            "inputs": user_message
        }

        response = requests.post(API_URL, headers=headers, json=payload)
        result = response.json()

        if isinstance(result, list) and "generated_text" in result[0]:
            reply = result[0]["generated_text"]
        else:
            reply = "Model error. Try again."

        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": "Server error occurred"}), 500
       
    

   
      
        
           
     
     

     
        