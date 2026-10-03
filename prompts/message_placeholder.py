from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage

#chat template
chat_template =ChatPromptTemplate([
    ('system','You are a helpful customer support agent.'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', '{query}') 

])

chat_history = []
#load chat history
with open('chat_history.txt', 'r') as f: 
    lines = f.readlines()
    chat_history.extend(lines)

print(chat_history)

#Create a prompt 
prompt = chat_template.invoke({'chat_history': chat_history, 'query': HumanMessage(content='Where is my refund')})

print(prompt)

