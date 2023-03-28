import requests

response0 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
response1 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
response2 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
response3 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response0.text)
print(response1.text)
print(response2.text)
print(response3.text)
