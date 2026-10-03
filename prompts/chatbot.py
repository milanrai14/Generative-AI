from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage


chat_model = ChatOllama(
    model='llama3.2'
)

chat_histoy = [
   SystemMessage(content="You are a helpful AI assistant.")
]

while True: 
   user_input=  input('You: ')
   chat_histoy.append(HumanMessage(content=user_input))
   if user_input == 'exit': 
      break
   result = chat_model.invoke(chat_histoy)
   chat_histoy.append(AIMessage(result.content))
   print("AI: ",result.content )

print(chat_histoy)