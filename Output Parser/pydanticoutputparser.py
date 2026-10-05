from langchain_core.output_parsers import PydanticOutputParser
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field


llm = ChatOllama(
    model="llama3.2"
)


class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(gt=18, description="Age of the person")
    city: str = Field(description="Name of the city")


parser = PydanticOutputParser(
    pydantic_object=Person
)


template = PromptTemplate(
    template="""
Generate ONE fictional {place} person.

The output MUST contain these three fields:
- name: person's actual name
- age: person's actual age
- city: person's actual city

Example of the required output:

{{
    "name": "Kamal Perera",
    "age": 25,
    "city": "Colombo"
}}

IMPORTANT:
Return actual person data.
Do NOT return the JSON schema.
Do NOT return "properties".
Do NOT return "description".
Do NOT return "title".
Do NOT return Python code.
Do NOT explain your answer.

Return ONLY the JSON object.

{format_instruction}
""",
    input_variables=["place"],
    partial_variables={
        "format_instruction": parser.get_format_instructions()
    }
)


chain = template | llm | parser


final_result = chain.invoke({
    "place": "Sri Lankan"
})


print("Result:")
print(final_result)

print("\nName:", final_result.name)
print("Age:", final_result.age)
print("City:", final_result.city)