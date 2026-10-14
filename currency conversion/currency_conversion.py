from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
import requests
from langchain_core.tools import InjectedToolArg
from typing import Annotated

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

# print("Conversion rate:", result)

@tool
def convert(base_currency_value: int, conversion_rate: Annotated[float, InjectedToolArg]) -> float:
    """
    Given a currency conversion rate this function calculates the target currency value from a given base currency value
    """
    return base_currency_value * conversion_rate

result = convert.invoke({'base_currency_value': 10, "conversion_rate": 95.345})
# print(result)

llm = ChatOllama(
    model='qwen2.5:3b', 
    temperature=0
)

#tool bindings
llm_with_tools = llm.bind_tools([get_conversion_factor, convert])

#tool calling
messages = [HumanMessage("What is the conversion factor between USD anfd NPR, and based on that can you convert 1o usd to npr ")]
# print(messages)
# print("*" * 50)
ai_message = llm_with_tools.invoke(messages)
messages.append(ai_message)
# print(ai_message.tool_calls)


for tool_call in ai_message.tool_calls:
    #execute the first tool and get the value of conversion rate
    if tool_call['name'] =='get_conversion_factor':
        tool_message1 =get_conversion_factor.invoke(tool_call)
        #fetch the conversion rate
        conversion_rate = tool_message1.content
        messages.append(tool_message1)
    #execute the second tool using the conversion rate from first tool
    if tool_call['name'] == "convert": 
        #fetch the current argument
        tool_call['args']['conversion_rate'] = conversion_rate
        tool_message2 = convert.invoke(tool_call)
        messages.append(tool_message2)

final_result = llm_with_tools.invoke(messages).content
print(final_result)