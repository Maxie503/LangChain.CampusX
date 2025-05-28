from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from langchain_core.output_parsers import PydanticOutputParser

from dotenv import load_dotenv

load_dotenv()


model = ChatGroq (model_name="llama3-70b-8192")

class person(BaseModel):
    name : str = Field(description='Name of the person')
    age : int = Field(description='Age of the person',gt=17)
    city : str = Field(description='Name of the city belongs to the person')


parser = PydanticOutputParser(pydantic_object=person)

template = PromptTemplate(template='Generate name, age, city of a fictional {place} person \
                          {format_instruct}',
                          input_variables={'person'},
                          partial_variables={'format_instruct':parser.get_format_instructions})


chain = template | model | parser

formattedResult = chain.invoke({'place':'bengali'})

print(formattedResult)