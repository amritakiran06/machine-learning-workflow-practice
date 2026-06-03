from groq import Groq

client = Groq(api_key="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")

prompt = "What is machine learning?"

response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

print("User Prompt:", prompt)
print("\nLLM Response:\n", response.choices[0].message.content)