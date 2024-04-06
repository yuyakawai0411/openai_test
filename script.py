from dotenv import dotenv_values
from openai import OpenAI

client = OpenAI(
    api_key=dotenv_values(".env").get("OPENAI_API_KEY")
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)
