# como hacer peticiones a APIs con Python
# con y sin dependencias

# 1. Sin dependencias (dificil y sin dependecias)
import urllib.request
import json

api_posts = "https://jsonplaceholder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_posts)
    data = response.read()
    json_data = json.loads(data.decode('utf-8'))
    print(json_data)
except urllib.error.URLError as e:
    print(f"Error en la solicitud: {e}")

# 2. Con dependencia (requests)
import requests

print("\nGet:")
api_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
print(response.json())

# 3. Un POST
print("\nPOST:")
try:
    api_posts = "https://jsonplaceholder.typicode.com/posts"
    input = {
        "title": "midu",
        "body": "dev",
        "userId": 5
    }

    response = requests.post(api_posts, json=input)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")

# 4. Un PUT
print("\nPUT:")
try:
    api_posts = "https://jsonplaceholder.typicode.com/posts"
    input = {
        "title": "midu",
        "body": "dev",
        "userId": 1
    }

    response = requests.put(api_posts, json=input)
    print(response.json())
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


import json

# Usar la API de OpenAI
OPENAI_KEY = ""
def call_openai_gpt(api_key, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_KEY}"
    }

    data = {
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, json=data, headers=headers)
    return response.json()

api_response = call_openai_gpt(OPENAI_KEY, "Escribe un breve poema sobre la programacion")
print(json.dumps(api_response, indent = 2))