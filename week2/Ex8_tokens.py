import time
import requests

resp1 = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
token = resp1.json()["token"]
seconds = resp1.json()["seconds"]
print(token, seconds)

resp_error = requests.get(
    f"https://playground.learnqa.ru/ajax/api/longtime_job", params=f"token=aaa{token}"
)
print(resp_error.json())

resp_status = requests.get(
    f"https://playground.learnqa.ru/ajax/api/longtime_job", params=f"token={token}"
)
print(resp_status.json())
time.sleep(seconds)

resp_seconds = requests.get(
    f"https://playground.learnqa.ru/ajax/api/longtime_job", params=f"token={token}"
)
print(resp_seconds.json())
