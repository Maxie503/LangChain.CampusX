from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

from dotenv import load_dotenv

load_dotenv()


model = ChatGroq (model_name="llama3-70b-8192")


scheme = [
    ResponseSchema(name='fact_1', description='Fact 1 about the topic'),
    ResponseSchema(name='fact_2', description='Fact 2 about the topic'),
    ResponseSchema(name='fact_3', description='Fact 3 about the topic')
    ]

parser = StructuredOutputParser.from_response_schemas(scheme)

template = PromptTemplate(template="Give three fact about the {topic} \n {format_instruct}",
                          input_variables=['topic'],
                          partial_variables={'format_instruct':parser.get_format_instructions()}
                          )

chain = template | model | parser

results = chain.invoke({'topic':'black hole'})

print(results)