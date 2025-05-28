from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

model = ChatGroq(model_name="llama3-70b-8192")



chat_hist = [SystemMessage(content="Yor are a helpful assistant")]

while True:
    user_input = input("You:")
    chat_hist.append(HumanMessage(content=user_input))
    if user_input == "exit":
        break
    results = model.invoke(chat_hist)
    print("AI:", results.content) 
    chat_hist.append(AIMessage(content=results.content))

print(chat_hist)


