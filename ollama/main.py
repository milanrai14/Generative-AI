from langchain_ollama import ChatOllama

#connect langchain to the locally installed llama model 

llm = ChatOllama(
    model= "llama3.2"
)

#send a prompt 
response = llm.invoke(
    "Explain artifical intelligence in simple word."

)
#print the model's response 
print(response.content)

