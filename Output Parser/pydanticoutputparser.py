from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field

llm = ChatOllama(
    model='llama3.2'
)

class Person(BaseModel): 
    name: str  = Field(description="Name of the person: ")
    age: int = Field(gt=18, description="Age of the person: ")
    city: str = Field(description="Name of the city the person belongs to ")
