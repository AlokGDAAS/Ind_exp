import os

path =r"C:\Users\DotNet\Desktop\Coding\Indi\P_inexpert"

def list_dir(n):
    return os.listdir(n)



def make_path(n):

    list=list_dir(n)
    pathlist ={}     
    for j in list:            
            pathlist[j] =os.path.join(n,j)

    
    print(f"There are {len(pathlist)} dir/file present in base directory ")
    for key in pathlist.keys():
         print(key)
    while(True):   
        option = input("Are you want to know list of direcotries of given directories yes/no : ") 
        if option == "yes":
            dir_name =input("Please enter diretory name : ")
            print(os.listdir(pathlist[dir_name]))
        elif option == "no":
             print("Nice to meet you")
             break
        else:
             print("Enter a correct option")    
       
        
        

make_path(path)








  
   



  