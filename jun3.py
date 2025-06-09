
id = int(input("Enter id : "))
name = input("Enter Name : ")
address = input("Enter Adress : ")
q1name = input("Enter q1name : ")
q1year = input("Enter q1year : ")
q2name = input("Enter q2name : ")
q2year = input("Enter q2year : ")
q3name = input("Enter q3name : ")
q3year = input("Enter q3year : ")

id2 = int(input("Enter id : "))
name2 = input("Enter Name : ")
address2 = input("Enter Adress : ")
q1name2 = input("Enter q1name : ")
q1year2 = input("Enter q1year : ")
q2name2 = input("Enter q2name : ")
q2year2 = input("Enter q2year : ")
q3name2 = input("Enter q3name : ")
q3year2= input("Enter q3year : ")

data =[
    {
        "id": id,
        "name" : name,
        "address": address,
        "qualification":
        [
            {
                "name": q1name,
                "year":q1year
            },
            {
                "name": q2name,
                "year":q2year
            },
            {
                "name": q3name,
                "year":q3year
            },

        ]
    },
    {
        "id": id2,
        "name" : name2,
        "address": address2,
        "qualification":
        [
            {
                "name": q1name2,
                "year":q1year2
            },
            {
                "name": q2name2,
                "year":q2year2
            },
            {
                "name": q3name2,
                "year":q3year2
            },

        ]
    },
]

print(data)