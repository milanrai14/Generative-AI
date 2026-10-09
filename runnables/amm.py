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