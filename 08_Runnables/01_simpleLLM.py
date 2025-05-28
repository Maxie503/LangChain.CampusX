from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

llm = ChatGroq(model_name="llama3-70b-8192", temperature=0.77)

prompt = PromptTemplate(
    input_variables=['topic'],
    template='Suggest a catchy blog titlt about {topic}'
    )

topic = input ('Enter a topic')


fromat_prompt =prompt.format(topic=topic)

blog_title = llm.predict(fromat_prompt)

print("\n\nBlog:",blog_title)