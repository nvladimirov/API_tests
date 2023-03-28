import requests


response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": 'GET'})

print(response.text)
