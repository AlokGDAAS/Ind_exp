def append_data(path,data):
    with open(path,"a") as file:
        file.write(data + "\n")
        print()

