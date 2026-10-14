from langchain_community.tools import DuckDuckGoSearchRun

search_tool = DuckDuckGoSearchRun() # DuckDuckGoSearchRun is also a runnables

results = search_tool.invoke("election of nepal")
print(results)

