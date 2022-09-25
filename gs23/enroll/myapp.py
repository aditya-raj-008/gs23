import requests
import json

URL="http://127.0.0.1:8000/enroll/studentcreateapi/"

#r=requests.get(url=URL)

#data1=r.json()
#print(data)

data={
    'cid': 111,
    'name':"alia",
    'email':"alia@gmail.com",
    } 

print(type(data))

json_data=json.dumps(data)
print(type(json_data))
r=requests.post(url=URL, data= json_data)
print("done till here",r)
#response
data=r.json()
print(data)
