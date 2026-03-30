#  1. WAP to ask the user to enter names of their 3 favorite movie & store them in a list.
# a = input("Your 1st favorite movie : ")
# b = input("Your 2nd favorite movie : ")
# c = input("Your 3rd favorite movie : ")
# Movie = [a,b,c]
# print(Movie)
# M-2
# movie = []
# movie.append(input("Your 1st favorite movie : "))
# movie.append(input("Your 2nd favorite movie : "))
# movie.append(input("Your 3rd favorite movie : "))
# print(movie)


# 2.WAP to check if a list contains a palindrome of a elements.(hint: use copy() method)
# Ex.: [1,2,3,2,1] or [3,"abs","abs",3]
list = ['m','a','a','m'] 
copy_list = list.copy()
copy_list.reverse()
if (list == copy_list):
    print("List is Palindrome")
else:
    print("List is not a Palindrome")    


#  3.WAP to count number of student with the 'A' grade in the following tuple
# ("C","D","A","A","B","D","A")
grade = ("C","D","A","A","B","D","A")
print("There are",grade.count("A"),"A Grade Student")

# 4. Store the above values in a list and sort them from "A to D"
# list = ["C","D","A","A","B","D","A"]
# list.sort()
# print(list)
