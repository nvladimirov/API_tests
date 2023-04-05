import requests
import pytest


class TestFirstApi:
    names = [("Vitalii"), ("Nikita"), ("")]

    @pytest.mark.parametrize("name", names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        resp = requests.get(url, params=data)

        assert resp.status_code == 200, "Неверный ответ сервера"

        resp_dict = resp.json()

        assert "answer" in resp_dict, "В ответе нет поля 'answer'"
        if len(name) == 0:
            expected_resp_text = "Hello, someone"
        else:
            expected_resp_text = f"Hello, {name}"
        assert resp.json()["answer"] == expected_resp_text, f"Actual name is not {name}"
