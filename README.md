# AI Chatbot with Conversation Memory

An interactive AI chatbot built using **LangChain, Groq LLM, Python, and Streamlit**.

## Features

- AI-powered conversational chatbot
- Conversation history using Streamlit Session State
- Context-aware responses using LangChain
- Groq LLM integration with GPT-OSS-20B
- Chat history clearing functionality
- Interactive Streamlit user interface
- Secure API key configuration using environment variables

## Tech Stack

- **Python** – Backend development
- **LangChain** – LLM orchestration and prompt management
- **Groq API** – LLM inference
- **Streamlit** – Frontend interface
- **python-dotenv** – Environment variable management

## Installation

Clone the repository:

```bash
git clone https://github.com/dinesh-reddy2005/Langchain-chatbot.git
cd langchain-chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project root and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Run the application:

```bash
python -m streamlit run frontend/app.py
```

## How It Works

1. The user enters a message through the Streamlit interface.
2. Previous messages are retrieved from Streamlit Session State.
3. LangChain formats the conversation using ChatPromptTemplate.
4. The Groq-hosted LLM generates a response.
5. The response is displayed and saved in conversation history.

## Future Enhancements

- Persistent chat history
- User authentication
- Retrieval-Augmented Generation (RAG)
- Document-based question answering
- Cloud deployment

## Author

Developed as a Generative AI project using Python, LangChain, Groq, and Streamlit.