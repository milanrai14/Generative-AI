from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

#model 
model = ChatOllama(
    model='llama3.2'
)

#prompt template 
prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}', 
    input_variables=['topic']
)

promt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the follwing text \n {text}',
    input_variables=['text']
)

#parser 
parser = StrOutputParser()

#building chain 
chain = prompt1 | model | parser | promt2 | model | parser

result = chain.invoke({'topic': 'Nepal'})
print(result)

#visualize the chain
chain.get_graph().print_ascii()