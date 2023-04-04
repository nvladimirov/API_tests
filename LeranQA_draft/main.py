import requests

# payload = {"name": "Nikita"} payload = {"name": "Nikita"}

response = requests.get(
    "https://auth.devmail.ru/cgi-bin/auth?Login=n.vladimirov@devmail.ru&agent=AG_gyQ3k7BoG9Difr2ZLXv10"
)
response.json()
print(response.json())
print(response.status_code)
