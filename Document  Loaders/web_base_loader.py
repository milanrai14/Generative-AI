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
    template="""
You are a helpful assistant.

Describe the topic: {topic}

Use the following webpage content as your source.
If the content does not contain relevant information,
say that the information is not available in the provided text.

Webpage content:
{text}

Write a clear explanation in simple English.
""",
    input_variables=["topic", "text"]
)


chain = prompt | model | parser

result = chain.invoke({'topic': 'Latahar tree regeneration and the impact of human activities on its population', 'text': docs[0].page_content})
print(result)
# print(len(docs))

# for doc in docs: 
#     print(doc.page_content)