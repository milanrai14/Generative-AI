#PAID API
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model = ChatAnthropic(models='claude-3.5-sonnet-20241022')

result = model.invoke("What is the capital of Nepal")

print(result)