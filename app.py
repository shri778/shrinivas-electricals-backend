from transformers import pipeline

# Load text-generation model
generator = pipeline("text-generation", model="gpt2")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"reply": "No message received"}), 400
    user_message = data["message"]

    try:
        result = generator(user_message, max_length=50, do_sample=True)
        reply = result[0]["generated_text"]
    except Exception as e:
        reply = "Model error: " + str(e)

    return jsonify({"reply": reply})
