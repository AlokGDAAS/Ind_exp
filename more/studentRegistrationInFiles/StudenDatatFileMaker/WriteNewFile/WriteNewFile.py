import json


def write_new_file(path,listData):       
        with open(path,"w") as file:
            file.write(json.dumps(listData,indent=4))
            print()
            print("File created successfully")
            print("="*60)



