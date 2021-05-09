phonebook = {} #create empty dictionary
phonebook["James"] = 6474589797
phonebook["ACAB"] = 911 #key associated with "James" in dictionary
print(phonebook)

for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))

#Name gets the value of the phonebook and number gets the key. 
# always ordered this way?


#Exercise
phonebook = {  
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
phonebook.pop("Jill")
phonebook["Jake"] = 938273443
print(phonebook)