# Streamlit Groq Chat App

This is a simple chatbot application built using Streamlit and Groq's API for generating chat responses. The app allows users to input a message and receive a response from the chatbot.

## Table of Contents
- [Installation](#installation)
- [Getting Groq API Key](#getting-groq-api-key)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Installation

### Prerequisites
- Python 3.8 or later
- Pip (Python package installer)
- Groq API Key (you can obtain this from the Groq platform)

### Step-by-Step Guide
1. **Clone the repository:**

    ```bash
    https://github.com/Raviteja-5976/Simple_Groq_API-usage.git
    cd Simple_Groq_API_usage
    ```

2. **Create a virtual environment:(optional but Recommended)**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required Python packages:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**

    ```bash
    streamlit run app.py
    ```

5. **Access the app:**
   Open your browser and go to `http://localhost:8501`.

## Getting Groq API Key

To use the Groq API, follow these steps to obtain your API key:

1. Go to [https://groq.com/](https://groq.com/).
2. Click on **Start Building**.
3. Login with your credentials or sign up if you don't have an account.
4. After logging in, click on **API key**.
5. Click on **New API key**.
6. Give your API key a name.
7. Copy the API key as it only shows once.

## Usage

### Interacting with the Chatbot
1. Enter your message in the text input field provided.
2. Click on the "Send" button.
3. The chatbot will generate a response and display it below your message.

### Example Interaction
- **User:** "Hello, how are you?"
- **Bot:** "I'm just a chatbot, but I'm here to help you!"

## Configuration

### API Key Setup
To use the Groq API, you need to configure your API key in the code. Replace the placeholder API key in the `Groq(api_key='your_api_key')` line with your actual API key.

```python
client = Groq(api_key='Your_API_Key')
