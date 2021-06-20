import requests
import json
URL = 'http://127.0.0.1:8000/stucreate/'   #target url
data = {'id':4 ,'name':'Shubham Bag','roll':104,'city':'Sonari'}  #python data 
json_data = json.dumps(data) #convert python data to json data
r = requests.post(url=URL,data=json_data)  
data=r.json()
print(data)