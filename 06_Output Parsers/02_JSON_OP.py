from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv

load_dotenv()


model = ChatGroq (model_name="llama3-70b-8192")

parser = JsonOutputParser()


template = PromptTemplate(
    template= "Give me name, age and city of fictional person \n {format_inst}",
    partial_variables={'format_inst' : parser.get_format_instructions()},
    input_variables=[]
    )


chain = template | model | parser

results = chain.invoke({})


print(results)



'''prompt = template.format()

result = model.invoke(prompt)

print('\n\n result',result)

print('\n\n result.content',result.content)

resultparse = parser.parse(result.content)

print('\n\npaerse result.content',resultparse)'''