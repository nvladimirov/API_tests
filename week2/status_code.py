import requests


response = requests.patch("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": 'GET'})

print(response.status_code)
