import requests
import json


URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data={}
    if id is not None:
        data = {'id' : id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    print(data)   
#get_data()

def post_data():
    data = {
        'name' : 'Munna',
        'roll' : 105,
        'city' : 'Mumbai'
    }
    json_data = json.dumps(data)
    headers = {'content-Type': 'application/json'}
    r = requests.post(url = URL, headers = headers, data = json_data)
    data = r.json()
    print(data)
post_data()

def partial():
    data = {
        'id' : 3,
        'name' : 'Ram',
        'city' : 'Ranchi'
    }
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
    
#partial()    
   

def put():
    data = {
        'id'  : 6,
        'name' : 'Ravina',
        'roll' : 103,
        'city' : 'Nashik',
        
        
    } 
    json_data = json.dumps(data)
    r = requests.put(url = URL, data = json_data)
    data = r.json()
    print(data)
    
#put()  


def delete_data():
    data = {'id' : 3 }
    json_data = json.dumps(data)
    r = requests.delete(url = URL, data = json_data)
    data = r.json()
    print(data)
    
    
#delete_data()    
    