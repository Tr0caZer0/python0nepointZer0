totalSumOfEvenRange = 0
for i in range(101):
    if (i % 2) == 0:
        totalSumOfEvenRange += i

print("Sum of the 100 first numbers is: " + str(totalSumOfEvenRange))