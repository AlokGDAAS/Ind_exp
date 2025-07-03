def Read_data(path):
    try:
        with open(path, "r") as file:
            data = file.read()
            return data
    except:
         return "There is some error try again"  



