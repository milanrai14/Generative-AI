from langchain_ollama import ChatOllama
from typing import TypedDict

class Review(TypedDict): 
    summary: str 
    sentiment: str 


model = ChatOllama(
    model='llama3.2'
)
structured_output = model.with_structured_output(Review)

result = structured_output.invoke("Great experience with good quality and easy-to-use features.Overall, I am satisfied and would recommend it to others.")


print(result)