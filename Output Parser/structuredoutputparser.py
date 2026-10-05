from langchain.output_parsers import StructuredOutputParser, ResponseSchema

response_schemas = [
    ResponseSchema(
        name="name",
        description="Name of the person"
    ),
    ResponseSchema(
        name="age",
        description="Age of the person"
    ),
    ResponseSchema(
        name="city",
        description="City where the person lives"
    )
]

parser = StructuredOutputParser.from_response_schemas(response_schemas)