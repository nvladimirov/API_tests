import json  # тут мы просто учимся парсить джейсон

string_as_json_format = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
obj = json.loads(string_as_json_format)

key = "messages"

if key in obj:
    print(obj[key][1])  # выводим только key из объекта
else:
    print(f"Ключа {key} в JSON нет")  # без f не заведется такой синтаксис
