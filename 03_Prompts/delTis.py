from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
# Create messages separately
system_message = SystemMessage(content='You are a helpful {domain} expert.')
human_message = HumanMessage(content='Explain in simple terms what is {topic}.')
# Create a ChatMessagePromptTemplate
chat_template = ChatMessagePromptTemplate(
    system_message=system_message,
    human_message=human_message
)
# Prepare the parameters for the template
parameters = {
    'domain': 'Cricket',
    'topic': 'Duck'
}
# Invoke the template with the specified parameters
prompt = chat_template.invoke(parameters)
# Print the generated prompt
print(prompt)