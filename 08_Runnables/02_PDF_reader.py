from langchain.document_loaders import TextLoader,Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

loader = Docx2txtLoader("C:\\Users\\U6056186\\Downloads\\OLDnewlevels.docx")

documents = loader.load()

text_split = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap = 50)

docs = text_split.split_documents(documents)

vectorstore = FAISS.from_documents(docs,OpenAIEmbeddings())


retriever = vectorstore.as_retriever()

query = "What are the key take away from the documents?"

retrieved_docs = retriever.get_relevant_documents(query)

retrieved_text = '\n'.join([docs.page_content for doc in retrieved_docs])

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.5)


prompt = f'Based on the following text , answer the question: \n \n {retrieved_text}'

answers = llm.predict(prompt)

print(answers)