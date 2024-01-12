income = int(input("Please provide monthly income: "))
tax = 0
if(income <= 38000 ):
    tax = income * 0.3
    print("Corresponding income tax: " + str(round(tax)))
elif((income > 38000) and (income <= 50000)):
    taxFive = (income - 38000) * 0.35
    print(taxFive)
    taxThirty = 38000 * 0.3
    print(taxThirty)
    tax = taxFive + taxThirty
    print("Corresponding income tax 5%: " + str(round(tax)))
else: 
    taxFive = (12000) * 0.35
    print(taxFive)
    taxFive2 = (income - 50000) * 0.40
    print(taxFive2)
    taxThirty = 38000 * 0.3
    print(taxThirty)
    tax = taxFive + taxThirty + taxFive2
    print("Corresponding income tax 5%: " + str(round(tax)))