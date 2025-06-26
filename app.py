from flask import Flask, request, jsonify
from flask_cors import CORS            # ← add
import json, os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})   # ← allow CORS for /api/*

# --------------------------------------------------------------------------
# Simple keyword-based Q&A store
# --------------------------------------------------------------------------
with open("profile_data.json") as f:
    data = json.load(f)

@app.route("/api/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "").lower()
    for item in data:
        if any(k in user_input for k in item["keywords"]):
            return jsonify({"response": item["answer"]})
    return jsonify({"response":
        "I'm not sure about that – check my résumé or GitHub!"})

@app.route("/", methods=["GET"])
def home():
    return "Chatbot backend running!"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
