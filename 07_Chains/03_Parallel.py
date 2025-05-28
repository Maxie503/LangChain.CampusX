from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableParallel
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(model_name="llama3-70b-8192")
parser = StrOutputParser()


template1 = PromptTemplate(template="Generate short and simple notes on the following text\n {text}",
                          input_variables=['text'])


template2 = PromptTemplate(template="Generate quiz 5 short question and answers about the following text:\n\n {text}",
                          input_variables=['text'])


template3 = PromptTemplate(template="merger the provided notes into a single documents \n\n {notes} and {quiz}",
                          input_variables=['notes', 'quiz'])




parallel_chain = RunnableParallel({'notes': template1 | model | parser,
                            'quiz' : template2 | model | parser
                            })

merge_chain = template3 | model | parser


finalChain = parallel_chain | merge_chain

results = finalChain.invoke({'text':'Black Hole'})


print(results)

finalChain.get_graph().print_ascii()
