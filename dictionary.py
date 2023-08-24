#unordered, changeable, adn not allowed duplicate values.

dictt={
    "name":"Raj",
    "age":25,
    "vehicle":"Thar",
    "DOB":"28-02-1998"
}

print(dictt)
print(len(dictt))
print(type(dictt))

x=dictt["vehicle"]
print(x)

x=dictt.get("vehicle")
print(x)

dictt["vehicle"]="BMW"     #to change the value in a dictionary
print(dictt)

dictt.update({"name":"Alden"})
print(dictt)

dictt.pop("vehicle")  #To remove the specific value
print(dictt)