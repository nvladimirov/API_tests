import requests

client_data = {"origin_skill_name": "radio"}
response = requests.post("https://vc1.go.mail.ru/phrase/create/event",
                         params={"client_data": "{\"origin_skill_name\": \"radio\"}", "event": "media.start_failed",
                                 "session_id": "e021ea0e-b692-46de-bb96-1d64ccced1a3",
                                 "device_id": ":c:m:android:23fc82a4e6c146b7a2730bba66924358",
                                 "skillserver_type": "gamma"})

print(response.json())
print(response.status_code)
