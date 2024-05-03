import requests
import json
import unittest

class TestSaveTokensToJson(unittest.TestCase):
    def setUp(self):
        self.url = "http://localhost:8000/app/api/v1/client"

    def test_path_tokens(self) -> None:

        send = {
            "email": "exampleandrian@gmail.com",
            "password": "fuck_you"
        }

        ext = "/login"
        response = requests.post(self.url + ext, json=send)

        raw_data = response.json()

        path = "/Users/yeray/Documents/GIT/GIT/Backend/tests/routes/client/restricted/data/"

        with open(path + 'data.json', 'r') as archivo:
            data = json.load(archivo)
        
        if response.status_code == 200:
            data["token_id"] = raw_data["token_id"]
            data["token_data"] = raw_data["token_data"]


            with open(path + 'data.json', 'w') as archivo:
                json.dump(data, archivo)

        print(raw_data)

        self.assertEqual(response.status_code, 200)

        


        

if __name__ == '__main__':
    unittest.main()