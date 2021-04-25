#For loops 
primes = [2, 3, 5, 7]

for prime in primes:
    print(prime)

#xrange and range
for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2): #why does this work?
    print(x)

#While loops
count = 0
while count <= 5:
    print(count)
    count = count + 1

#"break" and "continue"
count = 0
while True: #I.e. seemingly infinite loop, nothing to check
    print(count)
    count = count + 1
    if count >= 5:
        break # ends the loop.

#Printing out odd numbers using 'continue'
for x in range(10):
    if x % 2 == 0: #if x is divisible by 2
        continue #Return to loop beginning, starting at new index
    print(x)


#Can use else statements to execute upon termination of loops, but 'break' skips this execution 

