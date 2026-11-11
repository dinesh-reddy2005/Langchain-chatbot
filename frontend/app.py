import streamlit as st
import sys
import os

project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from backend.chatbot import generate_response

# Page Configuration
st.set_page_config(
  page_title="AI Chatbot", 
  page_icon="🤖"
)

# Application Title
st.title("AI Chatbot with Conversation History")
st.write("Hello! I can remember our previous conversation")

# Intialize chat History

if 'messages' not in st.session_state:
    st.session_state.messages = []

# Clear Chat History Button
if st.sidebar.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()


# Display Previous Messages

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Get User Input
user_question = st.chat_input("Ask me anything...")

if user_question:

    # Get Previous Conversation
    chat_history = st.session_state.messages.copy()

    # Display User Message
    with st.chat_message("user"):
        st.markdown(user_question)

        #Store User Messages
    st.session_state.messages.append({
        "role": "user", 
        "content": user_question
    })

    # Generate AI Response

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = generate_response(user_question, chat_history)
                st.markdown(response)

            except Exception as e:
                response = f"Error: {str(e)}"
                st.error(response)
                
# Store AI Response
    st.session_state.messages.append(
        {
        "role": "assistant", 
        "content": response
        }
    )

