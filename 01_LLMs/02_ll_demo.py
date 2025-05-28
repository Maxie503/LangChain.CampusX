from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


model = OpenAI(model='gpt-3.5-turbo-instruct')

results = model.invoke('Capital of india')


print(results)