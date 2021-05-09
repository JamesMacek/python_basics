#Modules are anything contained in a single .py script.

#importing modules. 





###Exercise. List all packages in re containing the string "find"
import re

print(dir(re))

for f in dir(re):
    if f == "find":
        print(f) #useless. No contents of "re" are called "find" 

    
for f in dir(re):
    if "find" in f: #useful. if f has substring "find"
        print(f) #solution to exercise. 

