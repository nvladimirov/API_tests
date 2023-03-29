import requests

method = "GET"

response_get = requests.get(
    "https://playground.learnqa.ru/ajax/api/compare_query_type?method=GET"
)

response_post = requests.post(
    "https://playground.learnqa.ru/ajax/api/compare_query_type?method=POST"
)

response_put = requests.put(
    "https://playground.learnqa.ru/ajax/api/compare_query_type?method=PUT"
)

response_delete = requests.delete(
    "https://playground.learnqa.ru/ajax/api/compare_query_type?method=DELETE"
)

response_head = requests.head(
    "https://playground.learnqa.ru/ajax/api/compare_query_type?method=HEAD"
)

response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(response_get.text)
print(response_post.text)
print(response_put.text)
print(response_delete.text)
print(response_head.status_code)
print(response.text)

catalog = ["GET", "POST", "PUT", "DELETE"]

for i in catalog:
    if i == "GET":
        data = "method=GET"
        response_get = requests.get(
            f"https://playground.learnqa.ru/ajax/api/compare_query_type?{data}"
        )
        response_post = requests.post(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_put = requests.put(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_delete = requests.delete(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        print(response_get.text)
        print(response_post.text)
        print(response_put.text)
        print(response_delete.text)
        print(" ")
    elif i == "POST":
        data = "method=POST"
        response_get = requests.get(
            f"https://playground.learnqa.ru/ajax/api/compare_query_type?{data}"
        )
        response_post = requests.post(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_put = requests.put(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_delete = requests.delete(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        print(response_get.text)
        print(response_post.text)
        print(response_put.text)
        print(response_delete.text)
        print(" ")
    elif i == "PUT":
        data = "method=PUT"
        response_get = requests.get(
            f"https://playground.learnqa.ru/ajax/api/compare_query_type?{data}"
        )
        response_post = requests.post(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_put = requests.put(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_delete = requests.delete(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        print(response_get.text)
        print(response_post.text)
        print(response_put.text)
        print(response_delete.text)
        print(" ")
    elif i == "DELETE":
        data = "method=DELETE"
        response_get = requests.get(
            f"https://playground.learnqa.ru/ajax/api/compare_query_type?{data}"
        )
        response_post = requests.post(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_put = requests.put(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        response_delete = requests.delete(
            "https://playground.learnqa.ru/ajax/api/compare_query_type", data=data
        )
        print(response_get.text)
        print(response_post.text)
        print(response_put.text)
        print(response_delete.text)
        print(" ")
