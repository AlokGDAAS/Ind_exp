student ={}

id = input("Enter id :")
student["id"] = id

name = input("Enter Name :")
student["id"] = name

add = input("Enter address :")
student["address"] = add




student["marks"]={}

Hmarks = int(input("Enter Hindi marks : "))

student["marks"]["Hindi"] = Hmarks

Emarks = int(input("Enter English marks : "))

student["marks"]["English"] = Emarks

Mmarks = int(input("Enter Maths marks : "))

student["marks"]["Maths"] = Mmarks

Smarks = int(input("Enter Science marks : "))

student["marks"]["Science"] = Smarks

Tmarks = Hmarks + Emarks + Mmarks + Smarks

Percentage = (Tmarks/400)*100


student["Percentage"] = Percentage

print(student)

# input
# id
# Name
# address
# marks

# {

# }

# output with percentage

# id
# Name
# address
# marks