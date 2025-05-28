from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

chat_hist= []

chat_template = ChatPromptTemplate([
    ('system','you are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_hist'),
    ('human','{query}')

])


with open ('3.Prompts\chat_hist.txt') as f:
    chat_hist.extend(f.readlines())

prompt = chat_template.invoke({'chat_hist':chat_hist,'query':'Where is my refund?'})  

print('\n\n\n',prompt)

