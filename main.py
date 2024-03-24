 import openai

# OpenAI API anahtarınızı buraya yerleştirin
openai.api_key = 'your_api_key_here'

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "GPT-3 Turbo API'sine nasıl istek gönderilir?"},
    ]
)

print(response["choices"][0]["message"]["content"])
