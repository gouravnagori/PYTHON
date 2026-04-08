student = {
    "Name" : "Gourav",
    "Branch": "CSE",
    "Section": "A",
    "Marks":{  #Nested Dictonary
        "DSA" : 90,
        "OOPS": 98,
        "Python":100

    },
    "HOD" : "Dr. Akhil Panday"

}
print(student)
student["Marks"]["SE"] = 93 #here we accessed or assign the value in the nested dictionary
# print(student["Marks"]["SE"])
print(student) 
 