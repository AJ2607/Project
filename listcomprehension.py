fruits=["Apple","Orange","Banana","grapes","Kiwi"]
"""newfruit=[]    # Declaring a new list

# To create a new list with fruits name with letter a from the old list.

for x in fruits:
    if "a" in x:
        newfruit.append(x)


print(newfruit)
"""
#listcomperehension

newfruit=[x for x in fruits if"a" in x]
print(newfruit)