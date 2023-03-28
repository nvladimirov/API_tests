import requests

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post(
    "https://playground.learnqa.ru/api/get_auth_cookie", data=payload
)

cookie_value1 = response1.cookies.get("auth_cookie")

cookies1 = {}
if cookie_value1 is not None:
    cookies1.update({"auth_cookie": cookie_value1})

response2 = requests.post(
    "https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies1
)

print(response2.text)
