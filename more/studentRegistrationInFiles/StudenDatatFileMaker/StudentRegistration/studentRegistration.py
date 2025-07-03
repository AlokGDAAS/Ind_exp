import datetime


def stu_reg_list(listData,path):    
      
    num = int(input("How many student do you want to register : "))
    for i in range(num):
        dict={}
        dict["id"]           = input("Please enter id : ")
        dict["name"]   = input("Please enter  name : ")
        dict["creation date"] = datetime.datetime.now().date().strftime("%d-%m-%Y")
        dict["creation time"] = datetime.datetime.now().time().strftime("%H:%M:%S")
        listData.append(dict)
        with open(path, "a") as file:
             file.write(str(dict)+"\n")


def stu_reg_dict():    

        dict={}
        dict["id"]           = input("Please enter id : ")
        dict["name"]   = input("Please enter  name : ")
        dict["creation date"] = datetime.datetime.now().date().strftime("%d-%m-%Y")
        dict["creation time"] = datetime.datetime.now().time().strftime("%H:%M:%S")
        return dict


      
            
            
         