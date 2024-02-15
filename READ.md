Below is a README.md template for your project. It includes instructions on navigating to the Google Cloud Console to retrieve the `application_default_credentials.json` file, which is necessary for authenticating your application with Google Cloud services.

```markdown
# AI Chat Interface

## Project Overview

This project implements an AI-powered chat interface using Flask, Google Cloud AI Platform, and Vertex AI. It enables users to interact with an AI in a chat session, supporting features such as sending messages, regenerating the last prompt, and editing the last prompt. The chat interface also supports markdown rendering for enriched text formatting.

## Features

- Send messages to an AI and receive responses in real-time.
- Regenerate the last prompt to explore different responses.
- Edit the last prompt for corrections or clarifications.
- Markdown support for text formatting in the chat interface.
- Chat history saved in a JSON file with a unique name at the end of each session.

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- Google Cloud account
- Google Cloud SDK

### Installation

1. Clone the repository:

   ```sh
   git clone https://your-repository-url.git
   cd ai-chat-interface
   ```

2. Install the required Python packages:

   ```sh
   pip install Flask google-cloud google-cloud-aiplatform
   ```

3. Obtain `application_default_credentials.json` from Google Cloud (see below).

4. Start the Flask application:

   ```sh
   python app.py
   ```

5. Access the chat interface at `http://127.0.0.1:5000/` in your web browser.

### Obtaining Google Cloud Credentials

To interact with Google Cloud services, you need to authenticate your application using a service account. Follow these steps to create a service account and download the `application_default_credentials.json` file:

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Navigate to the "IAM & Admin" > "Service accounts" section.
3. Click "Create Service Account", enter a name for the service account, and click "Create".
4. Grant the service account access to the necessary roles (e.g., AI Platform User, Storage Object Admin).
5. Click "Done" to create the service account.
6. Find the newly created service account in the list, click on the actions menu (three dots), and select "Manage keys".
7. Click "Add Key" > "Create new key", choose "JSON" as the key type, and click "Create".
8. The `application_default_credentials.json` file will be downloaded to your computer.

### Configuration

Place the `application_default_credentials.json` file in your project directory or specify its path in your application.

## Usage

After starting the Flask application and navigating to the provided URL, use the chat interface to interact with the AI. You can send messages, use the "Regenerate Last Prompt" and "Edit Last Prompt" buttons to modify the conversation, and end the chat session to save the history.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
```

This README provides a basic guide to getting your AI chat interface project up and running, including steps for obtaining the necessary Google Cloud credentials. Make sure to replace `https://your-repository-url.git` with your actual repository URL and adjust any specific instructions or prerequisites according to your project's setup.