from langchain_core.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel): 
    a: int = Field(required=True, description="The first number to add: ")
    b: int = Field(required=True, description="the second number to add: ")

    