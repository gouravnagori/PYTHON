# print("CODE FOR ODD AND EVEN")
# num = int(input("Enter an integer Number : "))
# if(num == 0):
#     print("Number is Zero") #we are giving the tab space(4 space) to execute the conditional statement, this is called identation in coding
# elif(num % 2 == 0):  #elif is only use when 1st statement is false
#     print(num,"is EVEN")
# else:               #we can write else only one time in a code
#     print(num,"is ODD")    

#Grade students Based on their marks
marks = int(input("Enter your marks out of 100 for grade : "))
if(100>=marks and marks>= 90):
    print("Grade = A")
elif(90> marks and marks>=80):
    print("Grade = B")
elif(80> marks and marks>=70):      
    print("Grade = C")
elif(70> marks and marks>=35):
    print("Grade = D")
elif(35> marks and marks>=0):  
    print("You are FAIL")
else:
    print(marks,"is not valid")


