number = 1 + 2*3/4.0 #appears to follow the order of operations. 
print(number)

#% is modulo division
#** is exponentiation

#String operators
helloworld = "Hello" + "" + "World"
print (helloworld)

lotsofhellos = "hello"*10 #
print(lotsofhellos)

#List operators
even_numbers = [2, 3, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = even_numbers + odd_numbers
print(all_numbers) #essentially concatenates the list 

print([1, 2, 3]*3) #can scale lists, creating repeating pattern

# Exercise
#Create two lists called x_list and y_list
x = object()
y = object()

x_list=([x]*10)
y_list=([y]*10)
print("x_list contains %d objects" % len(x_list))
xy_list = x_list + y_list
print("xy_list contains %d objects" % len(xy_list))