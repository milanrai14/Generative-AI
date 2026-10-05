from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


model = ChatOllama(
    model='llama3.2'
)

prompt = PromptTemplate(
    template='Generate 5 interesting facts about {topic}', 
    input_variables=['topic']
)

parser = StrOutputParser()

#with chain
chain = prompt | model | parser

result = chain.invoke({'topic': 'football'})

print(result)

#without chain
result = prompt.invoke({'topic': 'cricket'})
result2 = model.invoke(result)
result3 = parser.invoke(result2)
print(result3.content)