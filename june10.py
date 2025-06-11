# condition : Take user input (How many user you want)
# register students with qualification 

student_data = []

num = int(input("Enter number of students You want to add : "))

for n in range(num):
   dict ={}
   id = int(input("Enter id : "))
   dict["id"] = id
   name = input("Enter Name : ")
   dict["name"] = name
   address = input("Enter Address : ")
   dict["address"] = address
   dict["qualification"] = []
   
   while(True):
      subq ={}
      dec = input("Are you want to add qualifications yes/no ")
      if dec.lower() == "yes":
       subq["name"]=input("Please enter qualification name : ")
       subq["year"]=input("Please enter qualification year : ")

       dict["qualification"].append(subq)
      else:
        break
      
   if dict["qualification"]==[]:
        dict["qualification"] = "There is not any qualification given"
      

   student_data.append(dict)



print(student_data)