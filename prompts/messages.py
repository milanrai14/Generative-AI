from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

message_model = ChatOllama(
    model='llama3.2'
)

messages = [
    SystemMessage(
        content="You are a helpful assistant."
    ), 
    HumanMessage(
        content="Tell me about langchain."
    )

]

result = message_model.invoke(messages)

messages.append(AIMessage(result.content))

print(messages)