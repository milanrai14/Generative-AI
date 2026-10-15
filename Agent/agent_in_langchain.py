from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
import requests

search_tool = DuckDuckGoSearchRun()

result = search_tool.invoke("About sagarmatha")
print(result)