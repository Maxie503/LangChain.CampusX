from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenvlit
import streamlit as st


load_dotenv()
model = ChatGroq(model_name="llama3-70b-8192")

st.header("Story Generator")

genre = st.selectbox("Selecet Genere",['Fantasy','Sci-Fi','Mystery','Romance'])
main_char = st.text_input("Name of Main Character")
plot = st.text_area(" Describe the plot")

template = PromptTemplate(template="""
Write a {genre} story featuring a character named {main_char}.
plot: {plot}

Instructions:
1. Keep the story between 10 line
2. Include a clear beginning, conflict, and resolution.
3. Be imaginative but coherent.
""", input_variables=['genre','main_char','plot'], validate_template=True)

prompt = template.invoke({'genre':genre,'main_char':main_char,'plot':plot})
print(prompt)

if st.button("Generate Story"):
    response = model.invoke(prompt)
    st.write(response.content)