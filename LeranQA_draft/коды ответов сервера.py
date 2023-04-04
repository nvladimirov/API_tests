import requests

response = requests.get("https://learnqa.ru/", allow_redirects=False)
print(response.status_code)
