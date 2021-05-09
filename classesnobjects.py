#Classes are a way to organize code
class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class")

myobject = MyClass()

print(myobject.variable) #To access object within class, use this . notation 
myobject.function()

#Exercise
class Vehicle:
    name = ""
    kind = ""
    color = ""
    value = 0
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" %(self.name, self.color, self.kind, self.value) #Two decimal points in float
        return desc_str

car1 = Vehicle() #Assigning an object class to a particular car1
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

print(car1.description())
