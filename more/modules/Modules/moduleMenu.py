import module1
import module2
import module3

def menu():
    print("1. Register student ")
    print("2. Display student records")
    print("3. Display student records by id")
    print("4. Exit ")

def dashboardManagement():

    data=[]
    while(True):
        option = int(input("Enter your input : "))        

        if option == 1:
            d=module1.studentregistration()
            data.append(d)
        elif option  == 2:
            module2.get_syudent_record(data)
        elif option == 3:
            module3.SearchStubyId(data)
        elif  option == 4:
            break
      


menu()
dashboardManagement()