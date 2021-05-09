#appear to be optimal to use double quotes always!

astring = "Hello world!"
print(len(astring)) #12 characters long


print(astring.index("o"))
#astring is a string, which is an object that automatically changes substrings.
#hence the "." notation here. #all indexes start at 0 in python

print(astring.count("l")) #number of substrings in string

print(astring[3:7]) #Yup

#[start:stop:step] notation

#Reverse string using -1
print(astring[::-1]) #No numbers in start-step prints whole string

#Strings contain "upper" and "lower" functions
print(astring.upper())

#and startswith/endswith
print(astring.startswith("Hello")) #returns true

#Can split strings
print(astring.split(" ")) #Creates a 2-list with individual strings now


#Exercise: find string satisfying all conditions, including endswith and startswith

s = "Strings are awesome!" #Has length 20 -- solution
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a")) 

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))

