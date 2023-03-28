import requests

payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.values()
cookies = {'auth_cookie': cookie_value}
print(cookies)  # падает из-за ебучих скобок []

cookie_value1 = response1.cookies.get('auth_cookie')
cookies1 = {'auth_cookie': cookie_value1}
print(cookies1)
response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies1)

print(response2.text)
# print(response2.status_code)
# print(dict(response2.cookies))
# print(response2.headers)
