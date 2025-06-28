# with open("searchByQualificationMain.py", "r") as f:
#     content = f.read()
#     print(conten

path = r"C:\Users\DotNet\Desktop\tttt\sample.txt"

with open(path, "w") as f:
     f.write("""import Searchbyqualification

data =[]

def main():

    Searchbyqualification.student_registration(data)

    while(True):
        opt = int( input("Press 1 for print data and press 2 for search : "))
        if opt == 1:
            print(data)
        elif opt == 2:

            print(Searchbyqualification.search(data))



main()""")
    
    

