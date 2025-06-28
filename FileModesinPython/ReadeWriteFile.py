import json

path = r"C:\Users\DotNet\Desktop\tttt\sample.txt"

def create_dict(dict):
    

    dict["id"]= input("Please enter id : ")
    dict["name"]= input("Please enter name : ")
    dict["address"]= input("Please enter address : ")
    return dict

def WriteFile(n):
   
    with open(path,"w") as file:
        file.write(json.dumps(n,indent=4))
        print("File write successfully")


def ReadeFile():

    with open(path,"r") as file:
        data = file.read()
        print(data)

def prinfile():

    dict = {}

    create_dict(dict)
    
    

    while(True):
        option = int(input("Please enter a option : "))
        if option == 1:
            WriteFile(dict)
            
        elif option == 2:
            ReadeFile()    


prinfile()      


