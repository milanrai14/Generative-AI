from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model='llama3.2'
)

#1st prompt -> detailed report
template1 = PromptTemplate(
    template="Write a detailed report in {topic}", 
    input_variables=['topic']
)
#2nd prompt -> summary
template2 = PromptTemplate(
    template="Write a 5 line summary on the following text. /n {text}", 
    input_variables=['topic']
)

prompt1 = template1.invoke({'topic': 'black hole'})

result = model.invoke(prompt1)

promt2 = template2.invoke({'text':result.content })

result1 = model.invoke(promt2)


#with chain
parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic': 'black hole'})
print(result)