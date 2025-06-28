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
      