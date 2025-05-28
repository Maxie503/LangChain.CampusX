from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model_name="llama3-70b-8192")

messages = [SystemMessage(content="Yor are a helpful assistant"),
            HumanMessage(content="Tell me about LangChainin 5 lines")
            ]


results = model.invoke(messages)

messages.append(AIMessage(content= results.content))

print(messages)