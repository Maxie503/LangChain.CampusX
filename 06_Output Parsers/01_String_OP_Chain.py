from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()


model = ChatGroq (model_name="llama3-70b-8192")

template1 = PromptTemplate(template='Write a detailed report on {topic}', 
                          input_variables=['topic'])


template2 = PromptTemplate(template='Write five line summary the following  {text}', 
                           input_variables=['text'])


parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser


results=chain.invoke({'topic':"Black Hole"})

print(results)