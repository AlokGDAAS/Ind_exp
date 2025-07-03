import datetime


student_data = []
num = int(input("Enter number of students You want to add : "))
for n in range(num):
   dict ={}
   dict["id"] = int(input("Enter id : "))    
   dict["name"] = input("Enter Name : ")      
   dict["created on date"]  = datetime.datetime.now().date().strftime("%d-%m-%Y")
   dict["created on time"]  = datetime.datetime.now().time().strftime("%H:%M:%S")
   student_data.append(dict)

with open("student.txt","a") as file:
   for i in student_data:       
        file.write(str(i) + "\n")    
        print("File completed")



