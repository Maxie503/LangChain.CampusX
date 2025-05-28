from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
import os

os.environ['HF_HOME'] = 'C:/LangChain/huggingface_cached'

llm = HuggingFacePipeline.from_model_id(model_id='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task='text-generation', pipeline_kwargs=dict(temperature=0.5, max_new_token=100))

model = ChatHuggingFace(llm=llm)


results = model.invoke("Capital of USA??")

print(results.content)