from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(model_name="llama3-70b-8192")

template1 = PromptTemplate(template="Write detail report about a {topic}",
                          input_variables=['topic'])


template2 = PromptTemplate(template="Generate 5 pointer summary about the following text:\n\n {text}",
                          input_variables=['text'])

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model  | parser

results = chain.invoke({'topic':'black hole'})


print(results)

chain.get_graph().print_ascii()

