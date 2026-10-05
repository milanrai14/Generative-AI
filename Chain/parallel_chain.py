from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel


model = ChatOllama(
    model='llama3.2'
)

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Generare short and simple notes from the following text \n {text}', 
    input_variables=['text']
)
popularit_chain = prompt1 | model | parser

#Chain 2
prompt2 = PromptTemplate( 
    template='Generate 5 short question answer from the following text \n {text}', 
    input_variables=['text']
)
facts_chain = prompt2 | model | parser

#parallel chain 
parallel_chain = RunnableParallel(
    facts = facts_chain, 
    popularity = popularit_chain
)

result = parallel_chain.invoke({"text": "football"})

print("FACTS: ")
print(result['facts'])

print('\n Popularity')
print(result['popularity'])

print('*' * 100)
print(result)