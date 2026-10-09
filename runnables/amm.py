import random
class NakliLLM: 
    def __init__(self):
        print("LLM Created")

    def predict(self, prompt):
        response_list = [
            'KTM is the capital of Nepal', 
            'NPL is the cricket league.', 
            'AI stands for Artifical Intelligence'
        ]
        return {'response': random.choice(response_list)}

llm = NakliLLM()

result = llm.predict("What is the capital city of Nepal.")

print(result)

class NakliPromtTemplate: 
    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict): 
        return self.template.format(**input_dict)

template = NakliPromtTemplate(
    template="Write a {length} poem about {topic}", 
    input_variables=['length','topic']
)

result1 = template.format({'length': 'short','topic': 'inida'})
print(result1)