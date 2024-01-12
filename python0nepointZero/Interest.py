savings = int(input("Initial savings: "))
rate = int(input("Interest rate: "))
years = int(input("Number of years: "))

totalSaving = savings * (1+(rate/100))
print(totalSaving)
for i in range(years-1):
    totalSaving = totalSaving * (1+(rate/100))


print("The value of your savings after " + str(years) + " is " + str(round(totalSaving)))