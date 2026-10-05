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

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age, city of a ficiona {place} person \n {format_instruction}', 
    input_variables=['place'], 
    partial_variables={'format_instruction': parser.get_format_instructions()}
)