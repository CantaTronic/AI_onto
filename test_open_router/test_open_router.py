from openai import OpenAI
from config import cnf

client = OpenAI(
    base_url=cnf.API_BASE,
    api_key=cnf.API_KEY,
)
user_msg = 'Write "Test"'
messages = [
    {"role": 'user', "content": user_msg},
]
chat = client.chat.completions.create(
    model=cnf.API_MODEL,
    messages=messages,
)
reply = chat.choices[0].message.content
print(reply)
