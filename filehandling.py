"""
f=open("hi.txt","r")
#print(f.read())
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
#f.close  #close a file
"""

"""
f=open("hi.txt","w")
f.write("Had your lunch")
f.close()
f=open("hi.txt","r")
print(f.read())
"""

#f=open("AJ.txt","w") #x can also be used instead of x to create a new file


import os
os.remove("hi.txt") #used to remove a file
"""
import os
if os.path.exists("AJ.txt"):
    os.remove("AJ.txt")
else:
    print("File not present")
    """