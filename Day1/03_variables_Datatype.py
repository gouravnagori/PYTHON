# A variable is name given to a memory location in a program.
name = "Gourav Nagori"
age  = 19
address = "Kumbhalgarh"
hight = 184.3 #hight in cm
hight2 = hight
print(name)
print(age)
print(address)
print(hight2)
# Better way to write
print("\n")
print("My name is",name)
print("i am",age,"years old")
print("My hight is",hight)



# Rules for Identifiers/variables

# 1. Identifiers can be combination of uppercase and lowercase letters, digits or an underscore(_).
# So myVariable, variable_1, variable_for_print all are valid python identifiers.
# 2. An Identifier can not start with digit. So while variable1 is valid, 1variable is not valid.
# 3. We can't use special symbols like !,#,@,%,$ etc in our Identifier.
# 4. Identifier can be of any length.

# We can fint the type of a values with the help of type(name)
print("Types of variables")
print(type(name))
print(type(age))
print(type(hight2))

print("\n")
#other Data types
#boolean
voltage = True
voltage2 = False #T and F must be capital
print("Boolean data type")
print(voltage)
print(voltage2)
print(type(voltage))
#None - if we do not want to store data in variable then we can use None
gf = None
print(type(gf))
