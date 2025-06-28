import os

p =r"C:\Users\DotNet\Desktop\Coding\Indi\P_inexpert\Filemodesfiles"


def WriteFiles(path):    

    with open(path+"\sample2.txt" ,"w") as f:
        f.write("Hi I am Alok")
        print("successfull")


def ReadFiles(path):    

    with open(path+"\sample2.txt" ,"r") as f:
        data =f.read()
        print(data)


def ReadWriteFiles(n):

      

    while(True):  
        print("Press 1 for write file")        
        print("Press 2 for read file")      
        print("Press 3 for read exit")     

        while(True):
            option = input("Please enter an option : ")
            if option.isdigit():
                option = int(option)
                break
            else:
                print("Please enter a right number")
        if option == 1:
            while(True):
                num = input("How many files do you want to create : ")      
                if num.isdigit():
                    num = int(num) 
                    break
                elif int(num) >101 or int(num) <1:
                    print("You can create 1-100 files at a time")
                else:
                    print("Please enter a genuine number")

            for i in range(num):

                dir_path = n
                file_name = "\samp"+str(i+1) 
                extention = ".txt"  
                path = n+file_name+extention

                with open(path,"w") as f:
                    f.write("Hi developers ", i+1)
                    print("successfully created file ",i+1)
       



       
        elif option == 3:
            print("Thanks for using our service")
            break   
        else:
            print("Please give a right input") 

ReadWriteFiles(p)            




