from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough


model = ChatOllama(
    model='llama3.2'
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
   template='write a detailed report on {topic}', 
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}', 
    input_variables=['text']
)