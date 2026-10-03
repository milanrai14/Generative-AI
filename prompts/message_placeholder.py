from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

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
    chat_history.append(lines)

print(chat_history)