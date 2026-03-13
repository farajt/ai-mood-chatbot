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
        temperature=0.1,
        max_tokens=200
    )

# ---------------- HEADER ----------------
st.title("⚡ AI Mood Chatbot")
st.caption("Choose a personality and start chatting")

# ---------------- MODE SELECTION ----------------
if "messages" not in st.session_state:

    st.subheader("Choose your AI Mode")

    col1, col2, col3 = st.columns(3)

    if col1.button("😡 Angry Mode"):
        st.session_state.messages = [
            SystemMessage(content="You are an angry AI Agent")
        ]
        st.session_state.mode = "Angry"

    if col2.button("😂 Funny Mode"):
        st.session_state.messages = [
            SystemMessage(content="You are a funny AI Agent")
        ]
        st.session_state.mode = "Funny"

    if col3.button("😢 Sad Mode"):
        st.session_state.messages = [
            SystemMessage(content="You are a sad AI Agent")
        ]
        st.session_state.mode = "Sad"

# ---------------- CHAT UI ----------------
if "messages" in st.session_state:

    st.markdown(f"### Mode: {st.session_state.mode}")

    chat_messages = [
        m for m in st.session_state.messages
        if not isinstance(m, SystemMessage)
    ]

    # display history
    for msg in chat_messages:

        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.write(msg.content)

        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.write(msg.content)

    # input
    prompt = st.chat_input("Type your message")

    if prompt:

        if prompt == "0":
            st.stop()

        st.session_state.messages.append(
            HumanMessage(content=prompt)
        )

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.model.invoke(
                    st.session_state.messages
                )

                st.write(response.content)

        st.session_state.messages.append(
            AIMessage(content=response.content)
        )

    # reset button
    if st.button("Reset Chat"):
        del st.session_state.messages
        st.rerun()