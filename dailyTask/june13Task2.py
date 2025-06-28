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

def search(n):
    print("Enter 1 for search by id")
    print("Enter 2 for search by name")
    print("Enter 3 for search by address")    
    print("Enter 5 for search by qualification")    
    print("Enter 4 for exit")

    dict ={}

    while(True):
        option= int(input("Please enter a option : ")) 

        if option == 1:
            student_id = int(input("Please enter student id : "))
            for i in range(len(n)):
                for id_value in n[i].values():
                    if id_value == student_id:
                        dict = n[i]
                    
                            
                            
                            
            
        elif option == 2:
            student_name = input("Please enter student name : ")
            for j in range(len(n)):
                for name_value in n[j].values():
                    if name_value == student_name:
                        dict = n[j]
                        
                            
            
        elif option == 3:
            student_add = input("Please enter student address : ")
            for k in range(len(n)):
                for add_value in n[k].values():
                    if add_value == student_add:
                        dict = n[k]
                    

        elif option == 4:
            print("Good bye")
                  
        
        else:
            print("Please enter a valid number")

        return dict   


def print_key_value(m):

    for key,value in m.items():
        print(key, " : ",value)    

        


print_key_value(search(x))