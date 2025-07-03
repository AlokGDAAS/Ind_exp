
# data = [
#     {
#         "id":101,
#         "name":"alok",
        
#     },
#     {
#         "id":102,
#         "name":"garima",
        
#     },
#     {
#         "id":103,
#         "name":"durgesh",
        
#     },
# ]





def SearchStubyId(data):
    id = int(input("Plaese enter id : "))
    for dictData in data:
        if dictData["id"]== id:
            print(dictData)



