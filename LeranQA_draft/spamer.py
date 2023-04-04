import requests

# class TestPodcast:
#     def test_search_thematic_matching(self):
#         url = "https://vc1.go.mail.ru/setup_wizard/default_renders"
#         data = {"target_device_id": ":c:d:capsula_neo:1.42503050363333070045301B470475784250",
#                 "serial": "08011D4A2CF0DDB2"}
#         response = requests.get(url, params=data)
#         # import pdb
#         # pdb.set_trace()
#         print(response.json())

url = "https://vc1.go.mail.ru/setup_wizard/default_renders"
data = {
    "target_device_id": ":c:d:capsula_neo:1.42503050363333070045301B470475784250",
    "serial": "08011D4A2CF0DDB2",
}
i = 0
while i < 100:
    response = requests.get(url, params=data)
    print(response.json())
    i = i + 1
