from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

llm = ChatOllama(
    model='llama3.2'
)

