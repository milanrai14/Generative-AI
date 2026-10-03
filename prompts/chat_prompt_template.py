# For dynamic messages

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


# 1. Create Chat Prompt Template

chat_template = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful {domain} expert."
    ),
    (
        "human",
        "Explain in simple terms. What is {topic}?"
    )
])


# 2. Create Ollama Model

llm = ChatOllama(
    model="llama3.2",
    temperature=0.7
)


# 3. Create Chain


chain = chat_template | llm



# 4. Provide Dynamic Values
response = chain.invoke({
    "domain": "agriculture",
    "topic": "plant disease"
})


# 5. Print AI Response


print("AI:")
print(response.content)