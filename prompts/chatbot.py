from langchain_ollama import ChatOllama


chat_model = ChatOllama(
    model='llama3.2'
)

chat_histoy = []

while True: 
   user_input=  input('You: ')
   chat_histoy.append(user_input)
   if user_input == 'exit': 
      break
   result = chat_model.invoke(chat_histoy)
   chat_histoy.append(result.content)
   print("AI: ",result.content )

print(chat_histoy)