import datetime


student_data = []

num = int(input("Enter number of students You want to add : "))

for n in range(num):
   dict ={}
   dict["id"] = int(input("Enter id : "))    
   dict["name"] = input("Enter Name : ")    
   dict["address"] = input("Enter Address : ")  
   dict["created on date"]  = datetime.datetime.now().date().strftime("%d-%m-%Y")
   dict["created on time"]  = datetime.datetime.now().time().strftime("%H:%M:%S")
   # dict["qualification"] = []
   
   # while(True):
   #    subq ={}
   #    decision = input("Are you want to add qualifications yes/no ")
   #    if decision.lower() == "yes":
   #     subq["name"]=input("Please enter qualification name : ")
   #     subq["year"]=input("Please enter qualification year : ")

   #     dict["qualification"].append(subq)
   #    else:
   #      break
      
   # if dict["qualification"]==[]:
   #      dict["qualification"] = [{"There is not any qualification given"}]
      

   student_data.append(dict)



print(student_data)