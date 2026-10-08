from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

model = ChatOllama(
    model='llama3.2', 
    temperature=0
)

parser = StrOutputParser()

class Feedback(BaseModel): 
    sentiment: Literal['positive','negative'] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template="""
You are a sentiment classifier.

Classify the following feedback as either "positive" or "negative".

Feedback:
{feedback}

IMPORTANT:
Return ONLY valid JSON.
Do NOT return the JSON schema.
Do NOT return properties, required, title, or type.

The output must look exactly like:
{{"sentiment": "positive"}}

or:

{{"sentiment": "negative"}}

{format_instruction}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instruction": parser2.get_format_instructions()
    }
)



classifier_chain = prompt1 | model | parser2

# result = classifier_chain.invoke({'feedback': "this is a wonderful smaartphone"})
# print(result)

prompt2 = PromptTemplate(
    template= 'Write an approptiate response to this positive feedback \n {feedback}', 
    input_variables=['feedback']
)
prompt3 = PromptTemplate(
    template= 'Write an approptiate response to this negative feedback \n {feedback}', 
    input_variables=['feedback']
)
#Branching
branch_chain = RunnableBranch(
    (lambda x: x['sentiment'] == 'positive', prompt2 | model | parser), 
    (lambda x:x['sentiment']== 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not find the sentiment.")
)