
data = []

dict ={}

dict["id"] = int(input("Enter id : "))
dict["name"] = input("Enter Name : ")
dict["address"] = input("Enter Address : ")
dict["qualification"] = input("Enter qualification : ")

print(dict)

data.append(dict)

dict ={}

dict["id"] = int(input("Enter id : "))
dict["name"] = input("Enter Name : ")
dict["address"] = input("Enter Address : ")
dict["qualification"] = input("Enter qualification : ")

print(dict)

data.append(dict)

print(data)

id1 = data[0]["id"]
id2 = data[1]["id"]

name1 = data[0]["name"]
name2 = data[1]["name"]

add1 = data[0]["address"]
add2 = data[1]["address"]

qlf1 = data[0]["qualification"]
qlf2 = data[1]["qualification"]



items = input("Enter a item of list : ")

if items == "id":
    print("id 1 : ", id1)
    print("id 2 : ", id2)
elif items == "name":
    print("name 1 : ", name1)
    print("name 2 : ", name2)
elif items == "address":
    print("address 1 : ", add1)
    print("address 2 : ", add2)
elif items == "qualifications":
    print("qualification 1 : ", qlf1)
    print("qualification 2 : ", qlf2)
else:
    print("You enter a wrong input")