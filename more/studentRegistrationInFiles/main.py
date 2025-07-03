import StudenDatatFileMaker
import json



jsonfilepath ="studentData.json"
txtfilepath ="studentData.txt"
logsfilepath ="studentDataLogs.txt"

def main(jpath,tpath,lpath):
    username = input("Please enter your name : ")
    print()
    opt = input(f"""Welcome {username}
        I can help you to create txt files or json files
        at your given path and write/append data in files 
        and empty these files whenever you want. Are you want to proceed 
        with me    yes/no  """)
    print()
    if opt == "yes":
        try:
            prevData = StudenDatatFileMaker.Read_data(jpath)
            jsonData = json.loads(prevData)         
        except:
            jsonData =[] 

        flag = 0                  
            

        while(True):   
            if flag == 0:
               print(f"Good,choice {username} now choose your task \n")
               flag = 1
            else:
                print(f"Welcome back {username} now choose your task agin \n")   
            StudenDatatFileMaker.print_menu()
            option = int(input("Please enter your choice : "))
            if option == 1:
                print(f"\nGood choice, {username} you want to registaration of students let's start\n")
                while(True):
                    print()
                    choice = input(f"{username} In which file format you want to save your data txt/json ")
                    print()
                    if choice == "json":
                        print(f"\nGood choice, {username} you have choose to write a json file let's start\n")
                        
                        StudenDatatFileMaker.stu_reg_list(jsonData,lpath)
                        StudenDatatFileMaker.write_new_file(jpath,jsonData)
                        print(f"\n Well done, {username} you have successfully created json file \n")
                        print("="*60) 
                        break
                    elif choice == "txt":
                            num = int(input("How many student do you want to register : "))
                            print(f"\nGood choice, {username} you have choose to write a txt file let's start\n")
                            print()
                            for i in range(num):    
                                print(f"\nPease enter student {i+1} detail\n")                   
                                data = StudenDatatFileMaker.stu_reg_dict()
                                StudenDatatFileMaker.append_data(tpath,str(data))
                            print(f"\n Well done, {username} you have successfully appended data in your txt file \n")
                            print("="*60)  
                            break
            elif option == 2:
                print()
                choice = input("Which file's data do you want to read txt/json/both ")
                print()
                if choice == "txt":
                    print(StudenDatatFileMaker.Read_data(tpath) )  
                elif choice == "json":
                    print(StudenDatatFileMaker.Read_data(jpath))   
                elif choice == "both":
                    print("*"*60)
                    print("Text file data :-")
                    print()
                    print(StudenDatatFileMaker.Read_data(tpath) ) 
                    print()
                    print("\njson file data :- \n")
                    print(StudenDatatFileMaker.Read_data(jpath) ) 
                    print("*"*60)  
            elif option == 3:
                print()
                choice = input("Which file's data you want to remove txt/json/both ")
                print()
                if choice == "txt":
                    StudenDatatFileMaker.remove_Textfile_data(tpath) 
                    print(f"\n Well done, {username} you have successfully removed data from text file ")
                    print("*"*60 +"\n") 
                if choice == "json":
                    StudenDatatFileMaker.remove_jsonfile_data(jpath) 
                    print(f"\n Well done, {username} you have successfully removed data from json file ")  
                    print("*"*60 +"\n") 
                if choice == "both":
                    StudenDatatFileMaker.remove_Textfile_data(tpath)   
                    StudenDatatFileMaker.remove_jsonfile_data(jpath) 
                    print(f"\n Well done, {username} you have successfully removed data from both files ")  
                    print("*"*60 +"\n") 
            elif option == 4:
                print(f"Nice to meet you {username}")
                break
    else:
        print(f"Nice to meet you {username}")
                     


main(jsonfilepath,txtfilepath,logsfilepath)