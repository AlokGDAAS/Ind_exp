import json

def studentRegistration(listdata):    
      
    for n in range(2):
        dictData={}
        dictData["id"] =input("Please enter id : ")
        dictData["name"] =input("Please enter name : ")
        listdata.append(dictData)        
    with open("studentRecord.json" , "w")  as file:
               file.write(json.dumps(listdata,indent=4)) 
            

def readExistingData():
    
    with open("studentRecord.json" , "r") as file:
        data = file.read()
        return data


def prevData():
    output = json.loads(readExistingData()) 
    return output

def menu():
     print("Press 1 for student registration : ")   
     print("Press 2 for display student records : ")   
     option = int(input("Please enter your choice : "))
     prevData = prevData() 
     if option == 1:          
          if prevData:          
             studentRegistration(prevData)
          else:
               studentRegistration([])  
     elif option == 2:
          print(readExistingData())
     elif option == 3:
          print("Thanks for using our services")
     else:
          ("You have entered a wrong choice please try again") 
          

studentRegistration()


  