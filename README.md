# AI Mood Chatbot

A small Generative AI web application that allows users to chat with an AI that responds in different personalities.
The application is built using **Streamlit, LangChain, and Groq LLM** and demonstrates how prompt engineering can be used to control the behavior of an AI system.

Live interaction happens through a simple chat interface where users select a mood and then start a conversation with the AI.

---

## Project Overview

This project demonstrates how a single LLM can behave differently based on system instructions.

When the application starts, the user selects one of the available AI modes:

* Angry Mode
* Funny Mode
* Sad Mode

Once a mode is selected, the chatbot responds according to that personality during the entire conversation.

The system maintains conversation history during the session so the AI can respond with context.

---

## What This Project Demonstrates

This project focuses on practical GenAI application development and shows:

* Using **system prompts** to control AI behavior
* Building a **chat interface using Streamlit**
* Integrating **LangChain with Groq LLM**
* Managing conversation history using session state
* Structuring a small AI project for deployment
* Secure API key management using environment variables

The goal of this project is to demonstrate a simple but real-world GenAI workflow.

---

## Architecture

The application follows a simple conversational pipeline.

User Message
→ Streamlit Chat UI
→ LangChain Message Formatting
→ Groq LLM (Llama 3.1)
→ AI Response
→ Streamlit Display

Conversation history is stored in Streamlit session state so the model can generate context-aware responses.

---

## Tech Stack

### Backend

* Python
* LangChain
* Groq API (LLM inference)

### Frontend

* Streamlit

### Environment Management

* python-dotenv

### Deployment

* Streamlit Cloud
* GitHub

---

## How It Works

### Mode Selection

When the application loads, the user chooses one of the AI personalities.

Each personality sets a **system instruction** that defines the AI’s behavior.

Example:

* Angry mode → AI responds aggressively
* Funny mode → AI responds with humor
* Sad mode → AI responds in a melancholic tone

---

### Conversation Handling

User messages are stored in a session-based message list.

Each new message is appended to the conversation history and sent to the model.

LangChain formats the conversation before sending it to the Groq API.

---

### Response Generation

The Groq-hosted Llama model generates a response based on:

* The selected system instruction
* Previous conversation messages
* The user’s current input

The response is then rendered in the Streamlit chat interface.

---

## Project Structure

```
ai-mood-chatbot
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

**app.py**
Main Streamlit application containing the chatbot logic.

**requirements.txt**
Project dependencies.

**.env**
Stores environment variables such as the Groq API key.

**.gitignore**
Ensures sensitive files and environment folders are not pushed to GitHub.

---

## Installation

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-mood-chatbot.git
```

Move into the project directory:

```
cd ai-mood-chatbot
```

Create a virtual environment using uv:

```
uv venv
```

Activate the environment (Windows):

```
.venv\Scripts\activate
```

Install dependencies:

```
uv pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Add your Groq API key:

```
GROQ_API_KEY=your_api_key_here
```

You can generate a key from the Groq developer console.

---

## Running the Application

Start the Streamlit server:

```
streamlit run app.py
```

The application will open in your browser.

Typically at:

```
http://localhost:8501
```

Select a mode and start chatting with the AI.

---

## Possible Improvements

Future improvements for this project could include:

* Additional AI personalities
* Streaming responses for real-time typing
* Persistent conversation memory
* Conversation export
* UI enhancements
* Multi-model selection

---

## Author

Faraj Tamboli
M.Tech – Computer Science (AI)
IIIT Pune

Interested in applied AI systems, LLM engineering, and production-ready ML applications.
