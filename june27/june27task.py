import os
names = [
    "Aarav", "Vivaan", "Aditya", "Vihaan", "Arjun", "Sai", "Krishna", "Ishaan", "Kabir", "Rohan",
    "Ananya", "Aarohi", "Diya", "Ira", "Myra", "Saanvi", "Aadhya", "Avni", "Meera", "Riya",
    "Aryan", "Dhruv", "Kian", "Rudra", "Shaurya", "Yuvaan", "Om", "Dev", "Atharv", "Parth",
    "Kiara", "Navya", "Tara", "Aanya", "Nitya", "Anvi", "Prisha", "Samaira", "Vanya", "Zara",
    "Harsh", "Manav", "Nirav", "Rishi", "Siddharth", "Tanmay", "Uday", "Varun", "Yash", "Zayan",
    "Aditi", "Charvi", "Esha", "Gauri", "Ishita", "Jiya", "Kavya", "Lavanya", "Mahi", "Naina",
    "Ayaan", "Arya", "Chirag", "Darsh", "Eshan", "Gautam", "Harshil", "Ishan", "Jatin", "Kartik",
    "Leela", "Mira", "Nandini", "Ojasvi", "Pihu", "Radhika", "Sanya", "Tisha", "Urvi", "Vaishnavi",
    "Akhil", "Bhavya", "Chaitanya", "Devansh", "Eshwar", "Gopal", "Himanshu", "Iraja", "Jay", "Keshav"
]
profession_names = [
    "Doctor", "Engineer", "Teacher", "Nurse", "Scientist", "Artist", "Lawyer", "Chef", "Pilot", "Architect",
    "Dentist", "Pharmacist", "Veterinarian", "Journalist", "Photographer", "Designer", "Accountant", "Librarian",
    "Electrician", "Plumber", "Mechanic", "Carpenter", "Farmer", "Firefighter", "Police Officer", "Software Developer",
    "Data Analyst", "Web Developer", "Civil Engineer", "Surgeon", "Psychologist", "Therapist", "Musician", "Actor",
    "Writer", "Editor", "Translator", "Economist", "Biologist", "Chemist", "Physicist", "Astronomer", "Geologist",
    "Mathematician", "Statistician", "Social Worker", "Entrepreneur", "Marketing Manager", "Salesperson", "HR Manager",
    "Consultant", "Event Planner", "Real Estate Agent", "Bartender", "Waiter", "Barista", "Tailor", "Hairdresser",
    "Makeup Artist", "Fitness Trainer", "Athlete", "Coach", "Pilot", "Flight Attendant", "Customs Officer", "Judge",
    "Clerk", "Banker", "Stockbroker", "Insurance Agent", "Tour Guide", "Travel Agent", "Historian", "Archaeologist",
    "Anthropologist", "Zoologist", "Botanist", "Environmental Scientist", "Urban Planner", "Game Developer",
    "Animator", "Voice Actor", "Producer", "Director", "Choreographer", "Dancer", "Singer", "Radio Host", "TV Host",
    "Politician", "Diplomat", "Military Officer", "Security Guard", "Detective", "Forensic Scientist", "Paramedic",
    "Speech Therapist", "Occupational Therapist", "Counselor", "Researcher", "AI Specialist", "Robotics Engineer"
]

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
        print("Press 2 for see all files in your directory")      
        print("Press 3 for read all file content in your directory")     
        print("Press 4 for exit")     

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
                    
                    f.write(f"Hi I am {names[i]} . I am a {profession_names[i]} ")
                    print("successfully created file ",i+1)

        elif option == 2:
            list_dir = os.listdir(n)
            print(list_dir)     

            
        elif option == 3:
            list_dir = os.listdir(n)
            print(list_dir) 
            for j in range(len(list_dir)) :
                filepath = os.path.join(n,list_dir[j])   
                with open(filepath,"r") as f:
                    data = f.read()
                    print(list_dir[j]," : ",data)

        elif option == 4:
            print("Thanks for using our service")
            break   
        else:
            print("Please give a right input") 

        


ReadWriteFiles(p)

