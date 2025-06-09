import json


student = {

    "id": 1,
    "name": "Madhav",    
    "age": 25,
    "Qualification":"B.Tech (2020)",
    "email": "abc@gmail.com",
    "adress":"Aligarh"


}

print(json.dumps(student, indent = 4))
print(student)
print(student["id"])


#json.loads -> string to object
#json.loads -> object to string