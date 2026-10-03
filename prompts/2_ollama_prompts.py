from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()

# -----------------------------
# Ollama LLM
# -----------------------------
model = ChatOllama(
    model="llama3.2",
    temperature=0.7
)

# -----------------------------
# Test the model
# -----------------------------
result = model.invoke(
    "What is the capital city of Nepal?"
)

print(result.content)


# -----------------------------
# Streamlit UI
# -----------------------------
st.header("Research Tool")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    [
        "Beginner-Friendly",
        "Technical",
        "Code-Oriented",
        "Mathematical"
    ]
)

length_input = st.selectbox(
    "Select Explanation Length",
    [
        "Short (1-2 paragraphs)",
        "Medium (3-5 paragraphs)",
        "Long (detailed explanation)"
    ]
)


# -----------------------------
# Prompt Template
# -----------------------------
template = PromptTemplate(
    input_variables=[
        "paper_input",
        "style_input",
        "length_input"
    ],
    template="""
You are an expert research assistant.

Explain the following research paper:

Research Paper: {paper_input}

Explanation Style: {style_input}

Explanation Length: {length_input}

Please provide a clear and accurate explanation of the paper.

Cover:
1. The main problem
2. Proposed approach
3. Key concepts
4. Methodology
5. Important results
6. Why the paper is significant

Adapt the explanation according to the selected style and length.
"""
)


# -----------------------------
# Summarize Button
# -----------------------------
if st.button("Summarize"):

    prompt = template.invoke({
        "paper_input": paper_input,
        "style_input": style_input,
        "length_input": length_input
    })

    result = model.invoke(prompt)
    print(result.content)

    st.write(result.content)