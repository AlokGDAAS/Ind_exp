import module1
import module2

def menu():
    print("1. Register student ")
    print("1. Display student records")
    print("1. Exit ")

def dashboardManagement():
    option = int(input("Enter your input : "))
    if option == 1:
        module1.studentregistration()
    elif option  == 2:
        module2.