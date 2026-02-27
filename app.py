from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Jiraiya AI Backend is Running 🚀"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"reply": "No message received"}), 400

        user_message = data["message"].lower()

        # Simple AI logic
        if "hi" in user_message or "hello" in user_message:
            reply = "Hello! 😊 How can I help you?"
        elif "how are you" in user_message:
            reply = "I'm doing great! Thanks for asking 💪"
        elif "your name" in user_message:
            reply = "I am Jiraiya AI 🤖"
        else:
            reply = f"You said: {data['message']}"

        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": "Server error occurred"}), 500
       
    

   
      
        
           
     
     

     
        