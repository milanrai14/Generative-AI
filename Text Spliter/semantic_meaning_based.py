from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama.embeddings import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model='nomic-embed-text'
)
text_splitter = SemanticChunker(
    embeddings, 
    breakpoint_threshold_type="standard_deviation", 
    breakpoint_threshold_amount=1
)
sample = """
Python is a popular programming language.
It is widely used for machine learning.

The weather is sunny today.
The temperature is around 25 degrees.

Neural networks learn patterns from data.
Deep learning uses multiple neural network layers.
"""

docs = text_splitter.create_documents([sample])

print("Total chunks:", len(docs))
print("*" * 100)
for i, doc in enumerate(docs, start=1):
    print(f"\nChunk {i}:")
    print(doc.page_content)