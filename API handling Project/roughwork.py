import requests

url = "https://api.freeapi.app/api/v1/public/books/book/random"

response = requests.get(url)

database = response.json()

code = database.get("data")
print(code)