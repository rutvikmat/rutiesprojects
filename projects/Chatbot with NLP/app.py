from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# A simple set of rules for the chatbot
rules = {
    r'hello|hi|hey': 'Hello! How can I help you today?',
    r'how are you': 'I am just a bot, but I am doing great! Thanks for asking.',
    r'what is your name': 'I am a simple NLP Chatbot created in Python.',
    r'time': 'I cannot tell the time, sorry!',
    r'bye|goodbye': 'Goodbye! Have a great day.',
    r'.*': 'I am sorry, I do not understand that.' # Default response
}

def get_response(user_input):
    """Finds a matching rule and returns the corresponding response."""
    user_input = user_input.lower()
    for pattern, response in rules.items():
        if re.search(pattern, user_input):
            return response
    return rules['.*']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)