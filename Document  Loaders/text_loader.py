from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(
    model='llama3.2'
)

parser = StrOutputParser()


loader = TextLoader('football.txt', encoding='utf-8')

docs = loader.load()
print(docs)
print("=" * 50)
print(type(docs))
print(len(docs))
print("="*100)
print(docs[0])
print("="*100)
print(docs[0].page_content)
print("="*100)
print(docs[0].metadata)

prompt = PromptTemplate(
    template='Write a summany for the following text \n {text}',
    input_variables=['text']
)

chain = prompt | model | parser

result = chain.invoke({'text': docs[0].page_content})
print(result)