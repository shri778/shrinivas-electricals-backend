from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Backend is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400

    user_message = data["message"]

    try:
        # Example reply (you can change this later)
        reply = f"You said: {user_message}"
        return jsonify({"reply": reply})

    except Exception as e:
        return jsonify({"reply": "Error occurred"}), 500


if __name__ == "__main__":
    app.run(debug=True)

   


   
      
        
           
     
     

     
        