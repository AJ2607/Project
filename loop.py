y =[1,2,3,5,10,25,35,45,55,65,75,85,95,100,"js"]#To print each letters of a word declare the value as y="AJS"
for x in y:
    #print(x)
    if x==55:
       # break # breaks the loop
       continue #skips the declared value and print the other value.
    print(x)

"""
#prints the value till the declared range.
for x in range(50): # if the range value changed to 50,100 then it will print from 50 to 99.
    print(x) """

"""i=1
while i<10:
  i+=1
  if i==5:
     continue
  print(i)"""