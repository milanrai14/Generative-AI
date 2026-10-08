from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

model = ChatOllama(
    model='llama3.2'
)

parser = StrOutputParser()

class Feedback(BaseModel): 
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into positive or negative \n {feedback}', 
    input_variables=['feedback']
)

classifier_chain = prompt1 | model | parser

result = classifier_chain.invoke({'feedback': "this is a wonderful smaartphone"})
print(result)