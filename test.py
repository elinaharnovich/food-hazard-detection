import requests
import random

question_list = [
    "Tell me the main biological hazard found in smoked sausage",
    "Which allergen do biscuits contain?",
    "What types of foreign bodies were found in products?"
]
question = random.choice(question_list)

print("question: ", question)

url = "http://127.0.0.1:5000/question"


data = {"question": question}

response = requests.post(url, json=data)

print(response.json())
