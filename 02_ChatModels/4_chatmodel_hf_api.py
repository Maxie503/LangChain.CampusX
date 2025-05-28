from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

from dotenv import load_dotenv

load_dotenv()


llm = HuggingFaceEndpoint(model='deepseek-ai/DeepSeek-Prover-V2-671B',
                          task="text-generation"
                          )


model = ChatHuggingFace(llm=llm)


results = model.invoke("Whos is the PM of UK?")

print(results.content)