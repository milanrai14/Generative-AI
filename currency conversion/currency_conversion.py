from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
import requests

@tool
def get_conversion_factor(base_currency: str, target_currency: str)-> float:
    """
    This function fetches the currency conversion factor between a given base currency and a target currency
    """
    url = f"https://v6.exchangerate-api.com/v6/65cf317538c6f37cdc073ec6/latest/{base_currency.upper()}"

    response = requests.get(url)
    return response.json()


result = get_conversion_factor.invoke({"base_currency":"USD","target_currency": "INR"})
print(result)