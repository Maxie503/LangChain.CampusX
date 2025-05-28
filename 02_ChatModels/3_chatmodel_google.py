from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=1,max_tokens=50)

results= model.invoke("What is the capital of india?")

print(results.content)