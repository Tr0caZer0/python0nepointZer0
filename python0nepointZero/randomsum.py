import random
x = 0
myString = "Five random numbers: "
for i in range(5):
    randInt = random.randint(1,100)
    myString += str(randInt) + ' '
    x += randInt
print(myString)
print("The sum is " + str(x))