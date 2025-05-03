from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage
from dotenv import load_dotenv
from google.cloud import firestore
from langchain_google_firestore import FirestoreChatMessageHistory


load_dotenv()

PROJECT_ID = "langchain-50e8d"
SESSION_ID = "user_session"
COLLECTION_NAME = "chat_history"

print("initializing client")
client = firestore.Client(project=PROJECT_ID)

print("Initializing chat message history")

chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)

print("Chat history initialized")
print(f"current chat history is {chat_history.messages}")

llm = ChatOpenAI(model="gpt-4.1-mini",
                 temperature=0,
                 )

print("starting the AI type exit to exit ")


while True:
    query = input("You : ")
    if query.lower() == "exit":
        break

    chat_history.add_user_message(query)

    ai_response = llm.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI : {ai_response.content}")
    
    
  






