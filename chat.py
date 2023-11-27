from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def chat(input: str):
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": input }
    ]
    )
    completion = response['choices'][0]['message']['content']
    return completion