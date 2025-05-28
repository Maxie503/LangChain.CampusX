from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(model_name="llama3-70b-8192")

template1 = PromptTemplate(template='Write a detailed report on {topic}', 
                          input_variables=['topic'])

prompt1 = template1.invoke({'topic':"Black Hole"})

template2 = PromptTemplate(template='Write five line summary the following  {text}', 
                           input_variables=['text'])

promp2 = template2.invoke({'text':result1.content})


result1 = model.invoke(prompt1)

result2 = model.invoke(promp2)

print(result2.content)