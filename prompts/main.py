from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv
import streamlit as st 
from langchain_core.prompts import PromptTemplate


load_dotenv()




llm=HuggingFaceEndpoint(
    repo_id="meta-llama/Meta-Llama-3-8B-Instruct", 
    task="task_generation"
)

model = ChatHuggingFace(llm=llm)

result = model.invoke(
    "What is the capital city of Nepal?"
)

print(result.content)

st.header("Research Tool")
# user_input = st.text_input("Enter your prompt: ")
paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )


# Prompt template
template = PromptTemplate(
    input_variables=["paper_input", "style_input", "length_input"],
    template="""
You are an expert research assistant.

Explain the following research paper:

Research Paper: {paper_input}

Explanation Style: {style_input}

Explanation Length: {length_input}

Please provide a clear and accurate explanation of the paper.
Cover the main problem, proposed approach, key concepts, methodology,
important results, and why the paper is significant.

Adapt the explanation according to the selected style and length.
"""
)


#fill the place holdeer 
prompt = template.invoke({
    'paper_input': paper_input, 
    'style_input': style_input, 
    'length_input': length_input
})
if st.button("Summarize"): 
    result = model.invoke(prompt)
    st.text(result.content)