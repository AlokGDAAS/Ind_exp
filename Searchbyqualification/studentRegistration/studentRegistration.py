

def student_registration(d):
    
    while(True):
        num = input("Enter the number of student you want to add : ")
        if num.isdigit():
            num = int(num)
            break
        else:
            ("Please enter a number")

    for n in range(num):

        dict={}
        

        while(True):
            id = input(f"Please enter student {n+1} id:- ")
            if id.isdigit() and len(id)==3 and int(id)>0:
                dict["id"] = int(id)
                break
            else:
                print("Input is wrong please try again for id : ")

        while(True):
            name = input(f"Please enter student {n+1} name:- ")
            if name.isalpha():
                dict["name"] = name
                break
            else:
                print("Input is wrong please try again for name : ")

        while(True):
            address = input(f"Please enter student {n+1} address:- ")
            if name.isalnum():
                dict["address"] = address
                break
            else:
                print("Input is wrong please try again for name : ")

        dict["qualifications"]=[]     
        

        while(True):  
            subq={}                         
            decision = input(f"Are you want to add qualifications  yes/no ")
            if decision.lower() == "yes":
                while(True):
                    qualificationName = input(f"Please enter student {n+1} qualification name:- ")
                    if qualificationName:
                        subq["name"]=qualificationName
                        break
                    else:
                        print("Input is wrong please try again for qualification name : ")
                while(True):
                    qualificationYear = input(f"Please enter student {n+1} qualification year :- ")
                    if qualificationYear.isdigit() and len(qualificationYear) and int(qualificationYear)>0:
                        subq["year"]=qualificationYear
                        break
                    else:
                        print("Input is wrong please try again for qualification year : ")

                dict["qualifications"].append(subq)        

            elif decision.lower() == "no":
                break
            else:
                print("Please try again for qualification")
            

        d.append(dict)

    

           













