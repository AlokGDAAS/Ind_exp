import Searchbyqualification

data =[]

def main():

    Searchbyqualification.student_registration(data)

    while(True):
        opt = int( input("Press 1 for print data and press 2 for search : "))
        if opt == 1:
            print(data)
        elif opt == 2:

            print(Searchbyqualification.search(data))



main()