from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage

chat_template01 = ChatPromptTemplate(
    messages=[
        SystemMessage(content='You are a helpful {domain} expert.'),
        HumanMessage(content='Explain in simple terms what is {topic}.')
    ]
)


chat_template02 = ChatPromptTemplate([
    ('system','You are helpful {domain} expert'),
    ('human','Explain in simple terms, what is {topic}')
    ]) # this is given in langchain 0.3 version


parameters = {'domain': 'Cricket', 'topic':'Duck'}

prompt01 = chat_template01.invoke(parameters)

prompt01 = chat_template02.invoke(parameters)


print(prompt01)

