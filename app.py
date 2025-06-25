from flask import Flask, request, jsonify
import json

app = Flask(__name__)

with open('profile_data.json') as f:
    data = json.load(f)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '').lower()
    for item in data:
        if any(keyword in user_input for keyword in item['keywords']):
            return jsonify({"response": item['answer']})
    return jsonify({"response": "I'm not sure about that, but feel free to check my resume or GitHub!"})

@app.route('/', methods=['GET'])
def home():
    return 'Chatbot backend running!'

if __name__ == '__main__':
    app.run(debug=True)
