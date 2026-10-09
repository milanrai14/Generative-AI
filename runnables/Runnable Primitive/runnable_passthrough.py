from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.prompts import PromptTemplate

model = ChatOllama(
    model='llama3.2'
)

passthrough = RunnablePassthrough()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkdin post about {topic}', 
    input_variables=['topic']
)

parser = StrOutputParser()

