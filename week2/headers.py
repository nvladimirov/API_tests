import requests

headers = {"some_header": "123"}
response = requests.get(
    "https://playground.learnqa.ru/ajax/api/show_all_headers", headers=headers
)
print(response.json())
print(response.headers)

"""
{
  'result': {
    'Host': 'playground.learnqa.ru',
    'Port': '443',
    'X-Forwarded-For': '109.252.32.138',
    'X-Real-IP': '109.252.32.138',
    'X-Forwarded-Port': '443',
    'X-MH-Host': 'playground.learnqa.ru',
    'MH_GEOIP_COUNTRY_CODE': 'RU',
    'User-Agent': 'python-requests/2.27.1',
    'Accept-Encoding': 'gzip, deflate',
    'Accept': '*/*',
    'some_header': '123'
  }
}
"""
