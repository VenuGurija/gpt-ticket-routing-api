import openai

openai.api_key = "your-openai-key"

def route_ticket(text):
    prompt = f"Classify the following ticket: {text}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return {"category": response.choices[0].message["content"]}
