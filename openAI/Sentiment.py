from openai import OpenAI
import os

API_KEY=os.environ.get("OPEN_API_KEY")
client = OpenAI(api_key=API_KEY)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content

review = "The banana pudding was really tasty!"

prompt = f"""
Classify the following review as having either a positive or negative sentiment:
review: '''{review}'''
"""
response = get_completion(prompt)
print(response)