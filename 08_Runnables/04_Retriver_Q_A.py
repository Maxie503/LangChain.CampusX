from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains.retrieval_qa.base import RetrievalQA
from dotenv import load_dotenv
load_dotenv()

# document loaded
loader = TextLoader(r"C:\Users\U6056186\Downloads\Test.txt")
documents = loader.load()

# split the document
splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap = 50)
splited_doc = splitter.split_documents(documents)

# embedding of splited documents
vector_store = FAISS.from_documents(splited_doc,OpenAIEmbeddings())


# vector strore as retriver
retriever = vector_store.as_retriever()

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.5)


# Chaining of all components 

qa_chain = RetrievalQA(llm=llm,retriever=retriever)

# query

query = "What are the key take away from the documents?"

results = qa_chain.run(query)

print(results)