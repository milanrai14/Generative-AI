from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


model = ChatOllama(
    model='llama3.2'
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback}', 
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser

result = classifier_chain.invoke({'feedback': "this is a terrible smaartphone"})
print(result)