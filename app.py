import streamlit as st
from chatbot import get_response

st.title("Rule Based AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Enter your message.")

if user_input:
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    response = get_response(user_input)

    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])