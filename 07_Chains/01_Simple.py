from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


template = PromptTemplate(template="Write 5 line about a {topic}",
                          input_variables=['topic'])

model = ChatGroq(model_name="llama3-70b-8192")

parser = StrOutputParser()


chain = template | model | parser

results = chain.invoke({'topic':'wind'})


print(results)

chain.get_graph().print_ascii()

