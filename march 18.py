from groq import Groq

client = Groq(api_key="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")

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Explain AI in one line"}
    ]
)

print(response.choices[0].message.content)