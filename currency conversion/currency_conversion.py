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
    response.raise_for_status()
    data = response.json()

    if data.get("result") != "success":
        raise ValueError(f"API error: {data}")

    rates = data['conversion_rates']
    target = target_currency.upper()

    if target not in rates: 
        raise ValueError(f"Unsupported currency: {target}")
    
    return rates[target]


result = get_conversion_factor.invoke({
    "base_currency": "USD",
    "target_currency": "INR"
})

print("Conversion rate:", result)

@tool
def convert(base_currency_value: int, conversion_rate: float) -> float:
    """
    Given a currency conversion rate this function calculates the target currency value from a given base currency value
    """
    return base_currency_value * conversion_rate