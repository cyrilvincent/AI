from openai import OpenAI

with open("data/chatgpt/openai.env") as f:
    key = f.read()

with open("DL20-11-openai-code.py") as f:
    text = f.read()

print(text)

client = OpenAI(api_key=key)

nb = 5

completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"Voici un code Python, merci de me l'expliquer de manière concise, en {nb} points maximum, au format json"},
        {"role": "user", "content": text}
    ]
)

res = completion.choices[0].message
print(res.content)
