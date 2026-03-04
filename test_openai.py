from openai import OpenAI
import os

client = OpenAI()
try:
    response = client.embeddings.create(
        input="Olá mundo",
        model="text-embedding-3-small"
    )
    print("Sucesso!")
    print(response.data[0].embedding[:5])
except Exception as e:
    print(f"Erro: {e}")
