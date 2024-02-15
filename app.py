from flask import Flask, render_template, request, jsonify
from google.oauth2 import service_account
from google.cloud import aiplatform
from google.generativeai.types import safety_types
import vertexai
from vertexai.preview.generative_models import GenerativeModel, ChatSession

app = Flask(__name__)

# Initialize the AI chat session
chat_history = []

def init_chat():
    #Replace with your project_id
    project_id = "snappy-vim-149510"
    location = "us-central1"
    credentials = service_account.Credentials.from_service_account_file("./application_default_credentials.json")
    aiplatform.init(project=project_id, location=location, credentials=credentials)
    vertexai.init(project=project_id, location=location)
    # safety_setting. Second number is block. 1 - high block, 4 - none
    safety_setting = {
        1:1,
        2:1,
        3:1,
        4:1,
    }
    model = GenerativeModel("gemini-pro", safety_settings=safety_setting)
    chat = model.start_chat()
    return chat

chat_session = init_chat()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    response = get_chat_response(chat_session, user_message)
    return jsonify({'response': response})

def get_chat_response(chat: ChatSession, prompt: str) -> str:
    responses = chat.send_message(prompt, stream=True)
    return "".join(chunk.text for chunk in responses)

if __name__ == '__main__':
    app.run(debug=True)
