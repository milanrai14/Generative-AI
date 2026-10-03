from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st 

load_dotenv()




llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct", 
    task="task_generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke(
    "What is the capital city of Nepal?"
)

print(result.content)

st.header("Research Tool")
user_input = st.text_input("Enter your prompt: ")

if st.button("Summarize"): 
    result = model.invoke(user_input)
    st.text(result.content)