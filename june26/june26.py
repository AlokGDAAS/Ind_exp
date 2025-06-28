import datetime
import json


listdata =[]

for n in range(1,4):
    dictdata={}
    dictdata["id"]=input("Please enter sutdent id: ")
    dictdata["name"]=input("Please enter student name: ")
    dictdata["address"]=input("Please enter address: ")
    if n <3:
       dictdata["createddate"]=str(datetime.datetime.now().date())
    else:
        dictdata["createddate"]=str(datetime.datetime.now().date() + datetime.timedelta(days=2))
    listdata.append(dictdata)
print(json.dumps(listdata,indent=4))

result =[]

def search(n):
      
    dict ={}

    while(True):
        option= int(input("Please enter a option : ")) 

        if option == 1:
            date = input("Enter date in format yyyy-mm-dd : ")
            for i in n:
                for dd in i.values():
                    if dd == date:
                        result.append(i)

                  
        
        else:
            print("Please enter a valid number")

        return dict 
    

search(listdata)  
print(result)