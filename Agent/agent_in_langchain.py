from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_agent
from langchain import hub
import requests

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke("About sagarmatha")
# print(result)


llm = ChatOllama(
    model='qwen2.5:3b', 
    temperature=0
)

#step 2: Pull the ReAct prompt from the langchain hub
prompt = """
You are a helpful ReAct research agent.

Follow this process:
1. Reason about the user's question.
2. Decide whether a tool is needed.
3. Use the available tool when necessary.
4. Examine the tool's result.
5. Provide a clear final answer.

Use the search tool for factual questions that need external information.
"""

#step 3: create the ReAct agent manually with the pulled prompt
agent = create_agent(
    model=llm,
    tools=[search_tool], 
    prompt=prompt
)

