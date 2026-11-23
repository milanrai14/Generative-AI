# Generative AI 🚀

Welcome to my **Generative AI Learning Repository**!

This repository contains my hands-on learning journey in Generative AI, focusing on Large Language Models (LLMs), LangChain, Ollama, Retrieval-Augmented Generation (RAG), and building AI-powered applications.

The goal of this repository is to understand the core concepts of Generative AI and implement them through practical Python projects and experiments.

## 📚 Topics Covered

### 1. LangChain Fundamentals

- Agent Chains
- Chains and Runnables
- ChatModels
- LLMs (Large Language Models)
- Prompts and Prompt Templates
- Output Parsers
- Structured Output
- Tools and Tool Calling

### 2. Document Processing

- Document Loaders
- PDF Document Loading
- Text Document Loading
- Text Splitting
- Recursive Character Text Splitter
- Document Transformation

### 3. Embeddings and Vector Databases

- Embedding Models
- Text Embeddings
- Semantic Similarity
- Cosine Similarity
- Vector Stores
- Vector Database Operations
- Similarity Search

### 4. Prompt Engineering

- Prompt Templates
- Chat Prompt Templates
- System and Human Messages
- Dynamic Prompts
- Few-Shot Prompting
- Prompt Formatting

### 5. Output Handling

- String Output Parser
- JSON Output Parser
- Pydantic Output Parser
- Structured Output
- Response Formatting

### 6. Models and Ollama

- Open-Source LLMs
- Chat Models
- Ollama Integration
- Local LLM Execution
- Local Embedding Models
- Model Configuration

### 7. Retrievers and RAG

- Retrievers
- Vector Store Retrievers
- Similarity Search
- Retrieval-Augmented Generation (RAG)
- Document Retrieval
- Context-Based Question Answering

### 8. Conversation and Memory

- Conversation History
- Chat History
- Conversation Management
- Context-Aware Chatbots
- Chatbot Development

### 9. AI Tools and Agents

- Tool Integration
- Tool Calling
- Agent Concepts
- Agent Workflows
- LLM-Based Decision Making

## 🛠️ Technologies & Libraries

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Core programming language          |
| LangChain    | LLM application development        |
| LangGraph    | Stateful AI workflows              |
| Ollama       | Running local LLMs                 |
| ChromaDB     | Vector database                    |
| Hugging Face | Models and embeddings              |
| Pydantic     | Structured output validation       |
| Pytest       | Testing                            |
| NumPy        | Numerical operations               |
| Scikit-learn | Cosine similarity and ML utilities |

## 📂 Repository Structure

```text
Generative-AI/
│
├── Agent/
├── ChatModels/
├── DocumentLoaders/
├── Embedding-Models/
├── LLMs/
├── Output-Parsers/
├── Structured-Output/
├── Text-Splitters/
├── Tools/
├── Vector-Stores/
├── Prompts/
├── Ollama/
├── Retrievers/
├── Conversation/
├── Chatbot/
│
├── cosine_similarity.py
├── pytest.py
│
└── README.md
```

*The repository structure may evolve as I explore more concepts and implement additional projects.*

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/milanrai14/Generative-AI.git
```

Navigate to the project directory:

```bash
cd Generative-AI
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

Install the required libraries:

```bash
pip install langchain langchain-core langchain-community
pip install langchain-ollama langchain-chroma
pip install langchain-text-splitters
pip install chromadb pydantic
pip install numpy scikit-learn pytest
```

## 🦙 Ollama Setup

This repository also explores running open-source LLMs locally using Ollama.

Install Ollama from:

[https://ollama.com/](https://ollama.com/)

Download a model:

```bash
ollama pull llama3.2
```

Run the model:

```bash
ollama run llama3.2
```

Python integration:

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

response = llm.invoke("What is Generative AI?")

print(response.content)
```

## 🧪 Testing

Testing Python implementations using Pytest:

```bash
pytest
```

## 🎯 Learning Objectives

- Understand how Large Language Models work.
- Learn LangChain components and their integration.
- Explore local and open-source language models.
- Implement prompt engineering techniques.
- Understand document loading, splitting, and embedding.
- Work with vector databases and retrievers.
- Build conversational AI applications.
- Develop practical RAG-based applications.
- Understand AI agents and tool calling.

## 📈 Learning Progress

This repository is continuously evolving as I learn and experiment with new Generative AI concepts.

New implementations, experiments, and projects will be added regularly.

## 👨‍💻 Author

**Milan Rai**

BSc (Hons) Computing Student | AI Engineer Learner

- GitHub: [https://github.com/milanrai14](https://github.com/milanrai14)

---

⭐ If you find this repository useful, feel free to explore and star it!

**Learning Generative AI — One Implementation at a Time.**
