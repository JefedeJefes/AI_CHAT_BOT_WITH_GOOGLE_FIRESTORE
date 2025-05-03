from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from google.cloud import firestore
from dotenv import load_dotenv
from langchain_google_firestore import FirestoreChatMessageHistory

load_dotenv()


PROJECT_ID = "langchain-50e8d"
SESSION_ID = "lang_chain"
COLLECTION_NAME = "Chat_history"


client = firestore.Client(project=PROJECT_ID)


chat_history = FirestoreChatMessageHistory(
    session_id=SESSION_ID,
    collection=COLLECTION_NAME,
    client=client,
)


print(f"The chat history is {chat_history}")


"""initializing LLM"""

llm = ChatOpenAI(model="gpt-4.1-mini",
                 temperature = 0,)



#starting project 

while True:
    query = input("You : ")
    if query.lower() == "exit":
        break

    chat_history.add_user_message(query)

    ai_response = llm.invoke(chat_history.messages)
    chat_history.add_ai_message(ai_response.content)

    print(f"AI : {ai_response.content}")