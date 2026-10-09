from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough


model = ChatOllama(
    model='llama3.2'
)

passthrough = RunnablePassthrough()

print(passthrough.invoke({'name': 'haha'}))