from openai import OpenAI

client = OpenAI(api_key="sk-...", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "Output one of these four categories: 'indicator', 'ideation', 'behavior', 'attempt'."},
    ],
    max_tokens=3,
    stream=False
)

print(response.choices[0].message.content)