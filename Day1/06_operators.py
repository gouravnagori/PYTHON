# Types of operators
# An operator is a symbol that performs a certain operation between operands.

# · Arithmetic Operators ( +, -,*,/,% , ** )
# ** it is a power operator
a=2 
b=3
print(a**b) # a^b = 2^3 = 8

# · Relational / Comparison Operators ( == , != , > , < , >= , <= )
# when we use relational operators then we always get True or False in the output
print(a==b) #F
print(a!=b) #T
print(a>=b) #F
print(a<=b) #T

# · Assignment Operators ( = , +=, -= , *= , l=, %= , **= )
num = 12
num = num + 32 #or we can write num += 32
print("Num is",num)

num1 = 2
num1 -= 32 
print("Num1 is",num1)

num2 = 22
num2 /= 2 
print("Num2 is",num2)

# · Logical Operators ( not , and , or )
# logical operator works on boolean values.
print(not True)
print(not False)
a =283
b = 23
print(not a>b)

# and , or operators
x = True
y = False
print("and Operators is", x and y)
print("or Operators is", x or y)
print(a==b or a>b)
print(a>=b and b<a)