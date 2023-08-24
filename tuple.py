"""
list=("car","bike",25,25.7,True,'like')
print(type(list)) # If single value is declared then a comma should be added after the vale to define the type as tuple.

print(list[1:5])

"""

"""
 list.append("thar")
print(list)
tuple is unchangeable so not a single value can be added or modified 

"""

# changing tuple into list and changing value

z=("car","bike",25,25.7,True,'like')

y=list(z)
y[1]="Thar"

x=tuple(y)
print(x)
