getSum = int(input("Provide a three digit number: "))
sumOfThree = 0
while((getSum%10) != 0):
    sumOfThree += getSum%10
    getSum = getSum//10 
print(sumOfThree)