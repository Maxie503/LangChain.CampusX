from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
import streamlit as st

load_dotenv()

llm = HuggingFaceEndpoint(model='deepseek-ai/DeepSeek-Prover-V2-671B',task="text-generation")

model = ChatHuggingFace(llm=llm)

st.header('Welcome to PHub')

text = st.text_area('Please Paste the Reference full text').strip().split('\n')
features = st.text_area('Input all the features')
field = st.selectbox("Select the field of the Study",["Mechanical", 'Electrical', 'Electronic', 'Computers', 'Lifescience'])

template = PromptTemplate(
    template="""
You are an information extraction assistant.

Instructions:
1. Each item in the list below represents a **feature** to evaluate.
2. For **each feature**, output in the following format:
   - Feature X : PRESENT or ABSENT or INFERRED  : <feature name>
   - If PRESENT, include:
     Relevant text: <extracted text> [Paragraph or Claim No., if available]
3. If ABSENT, just mark the feature as ABSENT, but **do not repeat the missing feature immediately**.
4. After evaluating all features, **add a section at the end titled "Missing Features:"** and list only the feature names marked as ABSENT, one per line.
5. If the input size exceeds model limits, respond with: “Reduce your text size.”
6. Your answer must be in **plain text**, with no JSON or Markdown.

Field of Study is restricted to: {field}  
Features to Evaluate: {features}

Your task is to analyze the following text:  
{text}
""",
    input_variables=['field', 'text', 'features']
)


#print(features)
prompt = template.invoke({'field':field,'text':text,'features':features})

if st.button("Analyze the text"):
    results = model.invoke(prompt)
    st.write(results.content)

        
