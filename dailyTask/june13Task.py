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
            for i in n:
                for id in i.values():
                    if id == student_id:
                        dict = i

           

        elif option == 2:
            student_name = input("Please enter student name : ")
            for i in n:
                for name in i.values():
                    if name == student_name:
                        dict = i
                        
                            
            
        elif option == 3:
            student_add = input("Please enter student address : ")
            for i in n:
                for add in i.values():
                    if add == student_add:
                        dict = i
                        
                            
            
        elif option == 5:
            student_qlfy = input("Please enter student qualify : ")
            for i in n:
                for j in i.keys():
                    if j == "qualification": 
                        for k in i["qualification"]:
                            for qlfy in k.values():
                                if qlfy == student_qlfy:
                                    dict = i

                    

        elif option == 4:
            print("Good bye")
                  
        
        else:
            print("Please enter a valid number")

        return dict   


def print_key_value(m):

    for key,value in m.items():
        print(key, " : ",value)    

        


print_key_value(search(x))
