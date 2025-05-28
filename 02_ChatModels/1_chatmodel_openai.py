from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model='gpt-4o', temperature=1.5, max_completion_tokens=10)

results = model.invoke('Write 5 line poem')

print(results.content)