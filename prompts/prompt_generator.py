"""We can use single template for different uses according to it."""

from langchain_core.prompts import PromptTemplate

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
""", 
validate_template=True
)


template.save('template.json') # save the template in the json format.