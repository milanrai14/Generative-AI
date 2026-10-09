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

llm = NakliLLM()
