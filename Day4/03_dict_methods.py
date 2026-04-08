# Dictionary Methods

# myDict.keys() #returns all keys

# myDict.values() #returns all values

# myDict.items() #returns all (key, val) pairs as tuples

# myDict.get( "key"") #returns the key according to value

# myDict.update( newDict ) #inserts the specified items to the dictionary



student = {
    "Name" : "Rahul",
    "Age" : 20,
    "Marks":{
        "phy" : 74,
        "math" : 97,
        "chm" : 54,
    }
}
print(student.keys()) # it return all the keys but do not return the nested keys

# print(list[student.keys()]) #Type casting - convert Dict into list

print(len(student))

print(student.values()) #it will return all the values(Nested too)

print(student.items()) #returns all (key, val) pairs as tuples

# print(student["Name2"]) #it shows ERROR
print(student.get("Name2")) #No ERROR -> it shows None
student.update({"City":"Jaipur"})
print(student)

dict1={"Name" : "Gourav"
       }
dict2 = {"Surname": "Nagori"}
dict1.update(dict2)
print(dict1)
