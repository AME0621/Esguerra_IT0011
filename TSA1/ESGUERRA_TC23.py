#TSA1 letter A
n = 5 
for i in range(1, 6):
    print(" " * (n - i), end="") 
    for j in range(1, i + 1):  
        print(j, end="")  
    print()  

print() 

#TSA1 letter B.
for x in range (1, 6, 2):
    for y in range (0, x):
        print (x, end="")
    print(" ")

for x in range (6, 8):
    for y in range (0, x):
        print (x, end="")
    print(" ")