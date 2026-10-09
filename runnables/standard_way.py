import random
from abc import ABC, abstractmethod

class Runnable(ABC): 
    @abstractmethod
    def invoke(input_data): 
        pass

class NakliLLM(Runnable): 
    def __init__(self):
        print("LLM Created")
        
    def predict(self, prompt):
        response_list = [
            'KTM is the capital of Nepal', 
            'NPL is the cricket league.', 
            'AI stands for Artifical Intelligence'
        ]
        return {'response': random.choice(response_list)}
    
    def invoke(self, prompt):
        response_list = [
            'KTM is the capital of Nepal', 
            'NPL is the cricket league.', 
            'AI stands for Artifical Intelligence'
        ]
        return {'response': random.choice(response_list)}
    

class NakliPromtTemplate(Runnable): 
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict): 
        return self.template.format(**input_dict)

    
    def invoke(self, input_dict): 
        return self.template.format(**input_dict)


class NakliStrOutputParser(Runnable): 
    def __init__(self):
        pass

    def invoke(self, input_data):
        return input_data['response']

llm = NakliLLM()
template = NakliPromtTemplate(
    template='Write a {length} poem about {topic}', 
    input_variables=['length', 'topic']
)
parser = NakliStrOutputParser()

class RunnableConnector(Runnable): 
    def __init__(self, runable_list):
        self.runable_list = runable_list

    def invoke(self, input_data):

        for runable in self.runable_list:
            input_data = runable.invoke(input_data)
        return input_data

chain = RunnableConnector([template, llm, parser])
result = chain.invoke({'length': 'short', 'topic': 'Nepal'})
print(result)