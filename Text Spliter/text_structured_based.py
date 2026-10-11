from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
Python is a programming language.
It is easy to learn.

Machine learning is a branch of AI.
It learns patterns from data.

LangChain helps build LLM applications.
It supports retrieval and text processing.
"""

# initilize the splitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=80, 
    chunk_overlap=10,
)


#perfrom the split 
chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)