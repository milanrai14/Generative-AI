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

print('*'*50)
class NakliLLMChain: 
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict): 
        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)

        return result['response']

prompt1 = NakliPromtTemplate(
    template="Write a {length} poem about {topic}.",
    input_variables=['length', 'topic']
)

llm = NakliLLM()

#chain
chain= NakliLLMChain(llm=llm, prompt=prompt1)

result3 = chain.run({'length': 'short', 'topic': 'Nepal'})
print(result3)
