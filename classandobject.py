"""
# basic program

class human:
    x=5

h1=human()

print(h1.x)

"""

class Human:
    def __init__(aj,name,age): #aj is a parameter(any word can be used as parameter) used for reference of the class
        aj.name = name
        aj.age= age
    
    def methods(aj):
        print("Hi, My name is "+aj.name)



#h1= Human("Alden",25)
h1= Human("Stefi",23)
h1.methods()

del h1 # delete an object, will shoe error msg.
h1.name="Alden"
h1.age=25
h1.methods()
#print(h1.name)
#print(h1.age)