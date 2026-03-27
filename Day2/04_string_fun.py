# String Functions

# str = "I am a coder."

# str.endswith("er.") #returns true if string ends with substr

# str.capitalize() #capitalizes 1st char

# str.replace( old, new) #replaces all occurrences of old with new

# str.find( word ) #returns 1st index of 1st occurrence

# str.count("am") #counts the occurrence of substr in string

strn = "i am studing Python from ApnaCollege and i am a good guy and i am a student"
print(strn.endswith("lege"))
print(strn.capitalize()) #it creates a new string and change into it
print(strn.replace("Python","c++"))
print(strn.find("from"))
print(strn.find("fromsad"))#in this case the o/p is -1 (means it is not exist in our string or we can say that the -1 is as such is not a valid inbdex)
print(strn.count("am"))
print(strn.count("a"))
