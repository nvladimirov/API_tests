import requests

response = requests.get(
    "https://vc1.go.mail.ru/setup_wizard/default_renders?target_device_id=:c:d:capsula_neo:1"
    ".42503050363333070045301B470475784250&serial=08011D4A2CF0DDB2"
)
# first = response.history[0]
# second = response.history[1]
# third = response

# print(first.url)
# print(second.url)
# print(third.url)
