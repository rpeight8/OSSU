import requests
from dotenv import dotenv_values
import json

config = dotenv_values(".env")


url = "https://jsonplaceholder.typicode.com/todos/"
params = {
    "api_key": config["API_KEY"],
}

response = requests.get(url, params=params)
todos = response.json()

for todo in todos:
    print(todo)
