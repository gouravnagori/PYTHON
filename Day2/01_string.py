#String is the data type that store sequence of characters.

#\n is a escaps sequence character use for next line
str1 = "This is the string.\nThis is python language."
# print(str1)
#\t is a escaps sequence character use for tab space
str2 = "This is the string2.\tEveryone loves python language."
# print(str2)

#Basic Operation in string

# 1. concatination : Add two string with the help of + operator
# "Hello" + "World" = "HelloWorld"
print(str1 + str2)
print("\n")
# 2. length of string
#we can find the length of any sstring with the help of length function len(str)
print("Length of str1 is : ",len(str1))
print("Length of str2 is : ",len(str2))
print("Length of str1+str2 is : ",len(str1+str2))