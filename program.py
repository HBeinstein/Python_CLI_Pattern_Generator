import requests

response = requests.get("https://picsum.photos/200/300")
print(response.url)
