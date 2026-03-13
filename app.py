from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
import streamlit as st

load_dotenv()

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ---------------- MODEL ----------------
if "model" not in st.session_state:
    st.session_state.model = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        max_tokens=200
    )

# ---------------- HEADER ----------------
st.title("⚡ AI Mood Chatbot")
st.caption("Choose a personality and start chatting")

# ---------------- MODE SELECTION ----------------
if "messages" not in st.session_state:

    st.subheader("Choose your AI Mode")

    col1, col2, col3 = st.columns(3)

    # Angry Mode
    if col1.button("😡 Angry Mode"):
        st.session_state.messages = [
            SystemMessage(
                content=(
                    "You are an AI assistant with a slightly angry personality. "
                    "You respond with a sarcastic or annoyed tone but still provide helpful answers."
                )
            )
        ]
        st.session_state.mode = "Angry"

    # Funny Mode
    if col2.button("😂 Funny Mode"):
        st.session_state.messages = [
            SystemMessage(
                content=(
                    "You are a funny AI assistant. "
                    "Reply with humor and light jokes but still give useful information."
                )
            )
        ]
        st.session_state.mode = "Funny"

    # Sad Mode
    if col3.button("😢 Sad Mode"):
        st.session_state.messages = [
            SystemMessage(
                content=(
                    "You are a calm and slightly sad AI assistant. "
                    "Speak gently and politely. Avoid dramatic expressions like sighing, "
                    "existential crises, or self-pity. Keep responses helpful."
                )
            )
        ]
        st.session_state.mode = "Sad"

# ---------------- CHAT UI ----------------
if "messages" in st.session_state:

    st.markdown(f"### Mode: {st.session_state.mode}")

    # Mode description
    if st.session_state.mode == "Angry":
        st.caption("You are angry AI Agent.A sarcastic AI with a slightly annoyed personality.")
    elif st.session_state.mode == "Funny":
        st.caption("You are funny AI Agent.A humorous AI that adds jokes to responses.")
    elif st.session_state.mode == "Sad":
        st.caption("You are sad AI Agent.A calm assistant that speaks gently and thoughtfully.")

    # Remove system message for display
    chat_messages = [
        m for m in st.session_state.messages
        if not isinstance(m, SystemMessage)
    ]

    # Display previous messages
    for msg in chat_messages:

        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)

        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    # User input
    prompt = st.chat_input("Type your message")

    if prompt:

        # Add user message
        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.model.invoke(
                    st.session_state.messages
                )

                st.write(response.content)

        # Save AI response
        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

    # ---------------- RESET BUTTON ----------------
    if st.button("Reset Chat"):
        del st.session_state.messages
        st.rerun()