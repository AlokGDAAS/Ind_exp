def student_registration(): 
   student_data = []

   while(True):
     num = input("Enter number of students You want to add : ")
     if num.isdigit():
       num = int(num)
       break
     else:
       print("Please enter correct input : ")

   for n in range(num):
      dict ={}

      while(True):
         id = input("Enter id : ")
         if int(id) >0 and id.isdigit and len(id)==3: 
           dict["id"] = id   
           break
         else:
            print("Try again") 

      while(True):
         name = input("Enter name : ")
         if name.isalpha(): 
           dict["name"] = name 
           break
         else:
            print("Try again") 

      while(True):
         address = input("Enter address : ")
         if address.isalnum(): 
           dict["address"] = address 
           break
         else:
            print("Try again")       
      
      dict["qualification"] = []
      
      while(True):
         subq ={}
         decision = input("Are you want to add qualifications yes/no ")
         if decision.lower() == "yes":
         
            while(True): 
              subqn    =    input("Please enter qualification name : ")
              if subqn.isalnum(): 
                subq["name"]= subqn
                break
              else:   
               print("Please try again")
            while(True):
              subqy    =    input("Please enter qualification year : ")
              if subqy.isdigit() and len(subqn)==4 and int(subqy) > 0: 
                subq["year"]= subqy
                break
              else:
                print("Please try again")         

            dict["qualification"].append(subq)

         elif decision.lower() == "no":
             break
         else:
           print("try again")
         
      if dict["qualification"]==[]:
         dict["qualification"] = ["There is not any qualification given"]    

      student_data.append(dict)

   return student_data  

      
      
print(student_registration())

                  



