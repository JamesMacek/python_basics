def my_function(): #Does not have an argument (i.e. singleton function)
    print("Hello from My Function")

my_function()

def my_function_w_args(username, greeting):
    print("Hello, %s, I wish you %s" %(username, greeting))

name="Fruitycake"
greet="were Gay"
my_function_w_args(name, greet)

def sum(a, b): 
    return a + b #value retuned to output of the function

print(sum(1, 2))

#Exercise

def list_benefits():
    return "More organized code", "More readable code", "Easier code to reuse", \
    "Allowing programmers to share and connect code together"
   
x = list_benefits()
print(x)

def build_sentence(info):
    return info + " is a benefit of functions!"

print(build_sentence("gay"))