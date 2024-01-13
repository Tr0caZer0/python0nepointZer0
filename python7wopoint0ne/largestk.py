n = int(input("Enter a positive integer: "))
k = 0
y = 0

myString = " is the largest k such that "
for i in range(n):
    if ((i % 2) == 0):
        k += i
        if(k <= n):
            myString += str(i) + '+'
            y = i
        
myString = myString.rstrip(str(y)+'+')
print(str(y) +  myString + "+...+k < " + str(n))
            
            