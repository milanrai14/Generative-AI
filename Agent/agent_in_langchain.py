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
prompt = hub.pull("hwchase17/react")

#step 3: create the ReAct agent manually with the pulled prompt
agent = create_agent(
    llm=llm,
    tools={search_tool}, 
    prompt=prompt
)