from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model_name="llama3-70b-8192")
parser1 = StrOutputParser()


class feeback(BaseModel):
    sentiment : Literal ['Positive','Negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=feeback)

templates1 = PromptTemplate(template='Classify the sentimens of the following feedback {format} \n {feedback} \n ', input_variables=['feedback'], partial_variables={'format':parser2.get_format_instructions()})
templates2 = PromptTemplate(template='Write an approprate response ONLY for this Positive feedback with no extra infromation  \n {feedback} ', input_variables=['feedback'])
templates3 = PromptTemplate(template='Write an approprate response ONLY for this Negative feedback with no extra infromation  \n {feedback} ', input_variables=['feedback'])

classifier = templates1 | model | parser2

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'Positive', templates2 | model | parser1),
    (lambda x:x.sentiment == 'Negative', templates3 | model | parser1),
    RunnableLambda(lambda x:"Could not find the sentiments")
     )

final_chain = classifier | branch_chain

results = final_chain.invoke({'feedback':'Very very bad phone'})

print(results)