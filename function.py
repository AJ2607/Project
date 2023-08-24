"""
a=4
b=2
def jfunction():#defining a function
    print("a is even")
    #global a
    #a=1
    if a/2:
      print("a is odd")

    else:
      print("AJ")
   


jfunction()#calling a function
"""

def oe(n):
    if n % 2 == 0:
      return "even"
    else:
      return "odd"
    
number=int(input("Number:"))
r=oe(number)
print(f"Then {number} is {r}.")