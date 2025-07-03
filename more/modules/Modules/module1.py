def studentregistration():
    
    student ={}
    student["id"]=int(input("Please enter student id : "))
    student["name"]=input("Please enter student name : ")
    student["qualification"]=[
        {
            "name":"10th",
            "passing year":"2012",
        },
        {
            "name":"12th",
            "passing year":"2014",
        },
    ]
    
    return student