phonebook = {} #create empty dictionary
phonebook["James"] = 6474589797 #key associated with "James" in dictionary
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#Name gets the value of the phonebook and number gets the key. 
# always ordered this way?


