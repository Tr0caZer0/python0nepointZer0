import random

randomNumber = random.randint(-10,10)

print(randomNumber)

if((randomNumber % 2) == 0):
    if(randomNumber > 0):
        print(str(randomNumber) + " is positve and even")
    elif(randomNumber == 0):
        print(str(randomNumber) + " is even and neither positive nor negative")
    else:
        print(str(randomNumber) + " is negative and even")
else: 
    if(randomNumber > 0):
        print(str(randomNumber) + " is positve and odd")
    else: 
        print(str(randomNumber) + " is negative and odd")