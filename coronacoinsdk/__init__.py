import json

import requests
from requests.structures import CaseInsensitiveDict

class Client:
    url = "https://api.corona-coins.ru"

    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers["Content-Type"] = "application/json"

    # data = {
    #     "token": self.token,
    #     "method": method,
    #     "user_ids": users_ids
    # }

    def __init__(self,token):
        self.token = token

    def send_method(self,method,params):
        data = {
            "token": self.token,
            "method": method,
        }
        data.update(params)

        resp = requests.post(self.url, headers=self.headers, data=json.dumps(data))
        json_data = resp.json()
        if 'error' in json_data:
            print(f"Error: {json_data['error']}")
        else:
            return json_data["response"]


    def get_balance(self, users_ids):
        return self.send_method("score", {"user_ids": users_ids})


    def get_history(self, type, offset=0):
        return self.send_method("history", {"type": type, "offset": offset})

    def transfer(self, to_id, amount):
        if amount > 100000000000:
            return 'Максимальная сумма перевода составляет 100 000 000,000 коинов.'
        elif amount < 0:
            return 'Сумма перевода не может быть отрицательной.'
        else:
            return self.send_method("transfer", {"to_id": to_id, "amount": amount})





