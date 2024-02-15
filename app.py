from flask import Flask, render_template, request, jsonify
from google.oauth2 import service_account
from google.cloud import aiplatform
import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession
import json
import os
from datetime import datetime

app = Flask(__name__)

# Initialize the AI chat session

# Your existing init_chat and other functions here...


def init_chat():
    global chat
    #Replace with your project_id
    project_id = "snappy-vim-149510"
    location = "us-central1"
    credentials = service_account.Credentials.from_service_account_file("./application_default_credentials.json")
    aiplatform.init(project=project_id, location=location, credentials=credentials)
    vertexai.init(project=project_id, location=location)
    # safety_setting. Second number is block. 1 - high block, 4 - none
    safety_setting = {
        1:4,
        2:4,
        3:4,
        4:4,
    }
    model = GenerativeModel("gemini-1.0-pro", safety_settings=safety_setting)
    chat = model.start_chat()
    return chat

chat_session = init_chat()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/end_chat', methods=['POST'])
def end_chat():
    global chat

    # Convert chat.history to a string representation
    history_str = repr(chat.history)

    filename = f"chat_history_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    os.makedirs('chat_histories', exist_ok=True)
    with open(os.path.join('chat_histories', filename), 'w') as file:
        file.write(history_str)
    return jsonify({'message': 'Chat history saved successfully.', 'filename': filename})

### Need to be rewrited: https://ai.google.dev/api/python/google/generativeai/GenerativeModel#multi-turn
@app.route('/send_message', methods=['POST'])
def send_message():

    user_message = request.json['message']

    # Record the user's message


    response = get_chat_response(chat_session, user_message)

    # Record the AI's response


    return jsonify({'response': response})


def get_chat_response(chat: ChatSession, prompt: str) -> str:
    responses = chat.send_message(prompt, stream=True)
    return "".join(chunk.text for chunk in responses)

if __name__ == '__main__':
    app.run(debug=True)
