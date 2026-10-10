from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

url = "https://forestaction.org/iconic-latahar-tree/"

loader = WebBaseLoader(url)

docs = loader.load()

model = ChatOllama(
    model='llama3.2'
)

parser = StrOutputParser()

prompt = PromptTemplate(
    template='Describe the given topic \n {topic} from the following {text}', 
    input_variables=['topic', 'text']
)


chain = prompt | model | parser

result = chain.invoke({'topic': 'jackfuit', 'text': docs[0].page_content})
print(result)
# print(len(docs))

# for doc in docs: 
#     print(doc.page_content)