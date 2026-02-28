from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Shrinivas Electricals Assistant is Running ⚡"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"reply": "Please ask something."}), 400

        user_message = data["message"].lower()

        # Product replies
        if "fan" in user_message:
            reply = "Yes, we have ceiling fans and table fans available. Please visit Shrinivas Electricals, Nanded for prices."

        elif "mixer" in user_message:
            reply = "Yes, mixer grinders are available at Shrinivas Electricals."

        elif "wire" in user_message:
            reply = "We sell high-quality electric wires and PVC wire pipes."

        elif "bulb" in user_message or "led" in user_message:
            reply = "Yes, LED bulbs and lights are available in different watt options."

        elif "switch" in user_message or "board" in user_message:
            reply = "We have switch boards, switches and electrical fittings available."

        elif "iron" in user_message:
            reply = "Electric irons are available in our shop."

        elif "battery" in user_message:
            reply = "Yes, we sell batteries. Please visit for more details."

        # Shop information
        elif "time" in user_message or "open" in user_message:
            reply = "Shrinivas Electricals is open from 11 AM to 9 PM."

        elif "location" in user_message or "where" in user_message:
            reply = "We are located in Nanded. Visit Shrinivas Electricals for all electrical needs."

        elif "delivery" in user_message or "shipping" in user_message:
            reply = "Currently we do not provide home delivery. Please visit the shop directly."

        elif "contact" in user_message:
            reply = "Please visit Shrinivas Electricals in Nanded during working hours (11 AM - 9 PM)."

        elif "hi" in user_message or "hello" in user_message:
            reply = "Welcome to Shrinivas Electricals ⚡ How can we help you today?"

        else:
            reply = "We sell electrical items like fans, mixers, wires, bulbs, LED lights, switch boards, pipes, irons and batteries. Please ask about these items."

        return jsonify({"reply": reply})

    except Exception as e:
        print("Error:", str(e))
        return jsonify({"reply": "Something went wrong."}), 500