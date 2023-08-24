
n1 = int(input("Enter a number for n1: "))
n2 = int(input("Enter a number for n2: "))
num = int(input("Enter a number for number of terms: "))
print(n1)
print(n2)                
for i in range (1,num+1):
 n3=n1+n2
 n1=n2
 n2=n3
 print(n3)