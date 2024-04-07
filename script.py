from dotenv import dotenv_values
from openai import OpenAI

client = OpenAI(
  api_key=dotenv_values(".env").get("OPENAI_API_KEY")
)

prompt = input()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": prompt}
  ]
)

print(completion.choices[0].message.content)
