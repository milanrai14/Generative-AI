from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnableLambda, RunnablePassthrough

model = ChatOllama(
    model='llama3.2'
)

def word_count(text): 
    return len(text.split())

prompt = PromptTemplate(
    template='Write a joke about {topic}', 
    input_variables=['topic']
)

parser = StrOutputParser()


joke_gen_chain = RunnableSequence(prompt, model, parser)


paralle_chain = RunnableParallel({
    'joke': RunnablePassthrough, 
    ''
})