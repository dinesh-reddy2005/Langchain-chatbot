import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.prompts import(
    ChatPromptTemplate,
    MessagesPlaceholder
)

from langchain_core.messages  import  HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# Load Environment Variables
load_dotenv()

# Initialize the ChatGroq model
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7,
    groq_api_key=os.getenv("GROQ_API_KEY")
)

# Create a chat prompt template
prompt = ChatPromptTemplate.from_messages(
  [
    ("system", "You are a helpful AI assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{question}")
  ]
)

# Creating the chain
chatbot_chain = prompt | llm | StrOutputParser()

# Function to Generate Response

def generate_response(user_question, chat_history):
    
    # Convert List into Langchain Messages
    formatted_history = []
    for message in chat_history:
        if message["role"] == "user":
            formatted_history.append(HumanMessage(content=message["content"]))
        elif message["role"] == "assistant":
            formatted_history.append(AIMessage(content=message["content"]))

    
    # Generate the response using the chain
    response = chatbot_chain.invoke({
        "chat_history": formatted_history,
        "question": user_question
    })

    print("=================================")
    print(response)
    print("================================= ")
    return response

