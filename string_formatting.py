name = "James"

print("Hello, %s!" %name) #%s is the place where the string appears

#String and numeric 
#%s - string %d - int.. etc. 
age = 25
print("Hello %s, you are %d years old" %(name, age))

#Exercise
data = ("John", "Doe", 53.44) #ordered vector containing the data 
print("Hello %s %s. Your balance is $%s" %data) #Interesting. Must reorder the vectors as they appear?
#%s presents numeric as string fine. 