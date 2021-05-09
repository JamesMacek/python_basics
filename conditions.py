x = 2
print(x==2) #x==2 is a binary operator that yields true or false
print(x==3)
print(x<3)

name = "James" 
age = 25

if name=="James" and age == 25:
    print("Your name is James and you are 25 years old")

if name == "James" or name == "Gay":
    print("You are either named James or you are hella gay")

#In operator-- check to see if object is in a list
name = "James"
if name in ["James", "Rick"]:
    print("You are either James or Rick James, bitch") 

#'is' operator
x=[1, 2, 3]
y=[1, 2, 3]
print(x == y)
print(x is y)
print(x is x)

#but if, set x=y, now objects point to same value in memory
x=y
print(x is y)
#only temporarily...
y=2
print(x)


#Exercise 
# change this code to all admit "true"
number = 16
second_number = 10
first_array = []
second_array = [1,2,3]

if number > 15:
    print("1")

if not first_array: #If `object' asks if object is nonempty. 
    print("2")

if len(second_array) == 3:
    print("3")

if len(first_array) + len(second_array) == 3:
    print("4")

if not first_array and first_array[0] == 1:
    print("5")

if second_number:
    print("6")