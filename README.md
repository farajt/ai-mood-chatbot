# AI Mood Chatbot

A simple Generative AI web application where users can chat with an AI that responds with different personalities.
The chatbot is built using **Streamlit, LangChain, and Groq LLM** and demonstrates how system prompts can control AI behavior.

**Live App:** https://ai-mood-chatbot.streamlit.app
**Repository:** https://github.com/farajt/ai-mood-chatbot

---

## Project Overview

This project shows how a single LLM can behave differently depending on the instructions given to it.

The user selects an AI personality and then starts chatting.
Each personality is defined using a **system prompt**, which guides the tone and style of responses.

Available modes:

* Angry Mode
* Funny Mode
* Sad Mode

The application maintains conversation history during the session so the AI can respond with context.

---

## What This Project Demonstrates

* Prompt engineering using system instructions
* Building a chat interface with Streamlit
* Integrating LangChain with Groq LLM
* Managing conversation state using Streamlit session state
* Structuring a small GenAI application for deployment
* Deploying an AI app using Streamlit Cloud

This project focuses on creating a simple but complete LLM-powered application.

---

## Architecture

The application follows a straightforward conversational flow:

User Input
→ Streamlit Chat Interface
→ LangChain Message Handling
→ Groq LLM (Llama 3.1)
→ AI Response
→ Streamlit UI Display

Conversation history is stored in session state and sent with each request so the model can generate context-aware responses.

---

## Tech Stack

**Backend**

* Python
* LangChain
* Groq API (LLM inference)

**Frontend**

* Streamlit

**Environment Management**

* python-dotenv

**Deployment**

* Streamlit Cloud
* GitHub

---

## How It Works

**Mode Selection**

The user selects a chatbot personality.
Each mode sets a different system prompt that controls the AI's behavior.

**Conversation Handling**

User messages and AI responses are stored in session state to maintain chat history.

**Response Generation**

The conversation history is sent to the Groq-hosted Llama model, which generates the response based on the selected personality.

**UI Rendering**

Streamlit displays messages in a chat interface and updates the conversation in real time.

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

---

## Possible Improvements

Future improvements could include:

* Additional AI personalities
* Streaming responses (real-time typing)
* Persistent chat history
* UI enhancements
* Model selection options

---

## Author

Faraj Tamboli
M.Tech CSE (AI) — IIIT Pune
