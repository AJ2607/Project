# lists are ordered, changeable and allow duplicates

list=["car","bike",25,25.7,True,'like']
print(list)
print(len(list)) # length of the list.
print(type(list)) # list type.
print(list[2:5]) # Prints the specified values of the list.

list[1:3]=["plane"]# to change the values inside the list, if square bracke removed each letter will be printed seperately.
print(list)

list.insert(3,"jeep") # To insert a new value inside the list
print(list)

list.append("Thar") # To insert a new value at the end of the list
print(list)

list.remove("Thar") #To delete the selected value
print(list)