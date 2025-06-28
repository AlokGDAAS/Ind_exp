
data = [1,{
            "id":101,
            "name":"Alok",
            "address":"aligarh"
      },3]

y = [
      {
            "id":101,
            "name":"Alok",
            "address":"aligarh"
      },
      {
            "id":102,
            "name":"Garima",
            "address":"agra"
      },
      {
            "id":103,
            "name":"Durgesh",
            "address":"Dibai"
      },
]

x=[
{
    "id":101,
    "name":"Alok",
    "address":"aligarh",
    "qualifications":[
        {
            "name":"10th.",
            "year":2012
        },
        {
            "name":"12th",
            "year":2014
        },
        {
            "name":"B.A.",
            "year":2017
        },
    ]
},
{
    "id":102,
    "name":"Garima",
    "address":"agra",
    "qualifications":[
        {
            "name":"10th.",
            "year":2013
        },
        {
            "name":"12th",
            "year":2015
        },
        {
            "name":"B.Sc.",
            "year":2018
        },
    ]
},
{
    "id":103,
    "name":"Durgesh",
    "address":"Dibai",
    "qualifications":[
        {
            "name":"10th.",
            "year":2017
        },
        {
            "name":"12th",
            "year":2019
        },
        {
            "name":"B.Com.",
            "year":2022
        },
    ]
},
]




data2 = {
            "id":101,
            "name":"Alok",
            "address":"aligarh"
      }

# for i in n:
#     print(i)

def print_key_value(n):
    for key,value in n.items():
        print(key,":",value)


for i in x:
    for j in i["qualifications"]:
        print_key_value(j)


    
                   






