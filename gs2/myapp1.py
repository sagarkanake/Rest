import requests
import json
URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'name' : "seeta",
    'roll' : 106,
    'city' : "nashik"
}

json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)
print("sagar")
data = r.json()
print(data)


