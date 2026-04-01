# Dictionary in Python
# Dictionaries are used to store data values in key:value pairs

# They are unordered(no indexing), mutable(changeable) & don't allow duplicate keys

# dict = {
# "name" : "shradha",
# "cgpa" : 9.6,
# "marks" : [98, 97, 95],
# }
# "key" : value

# dict["name"], dict["cgpa"], dict["marks"]

# dict["key"] = "value" #to assign or add new

# We can make list and dict as a key because they are mutable(can be change)
information = {
    "Name" : "Gourav",
    "Age"  : 19,
    "Hight": 184.3,
    "SGPA" : [8.6, 8.6, 9.0],
    "Address": "Jaipur",
    12 : 2
}
print(information)
print(type(information))
print(information["Name"])
print(information["SGPA"])
information["Salary"] = 9000000
print(information["Salary"])
information["Name"] = "Chirag"
print(information)


null_dict = {}
print(null_dict)
null_dict["Name"] = "Koushal Asawa"
print(null_dict)