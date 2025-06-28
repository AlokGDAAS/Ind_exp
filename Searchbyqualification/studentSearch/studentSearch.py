


def search(n):


    print("Enter 1 for search by id")
    print("Enter 2 for search by name")
    print("Enter 3 for search by address")    
    print("Enter 4 for search by qualification")    
    print("Enter 5 for exit")
    
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
                        
                            
            
        elif option == 4:
             result = []
             option = input("Enter qualification : ")
             for i in n:
                for qualification in i["qualifications"]:
                    if qualification["name"].lower() == option.lower():
                        result.append(i)
                        dict = result
                    

        elif option == 5:
            print("Good bye")
                  
        
        else:
            print("Please enter a valid number")

        return dict   
    
    