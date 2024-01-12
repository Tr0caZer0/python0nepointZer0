price = float(input("Price: "))
payment = float(input("Payment: "))

change = int(payment - round(price))
print(change)

while change != 0:
    bill = change // 1000
    if bill > 0:
        print("1000kr bills: " + str(bill))
    else:
        print("1000kr bills: " + str(0))
    change = change % 1000

    bill = change // 500
    if bill > 0:
        print("500kr bills: " + str(bill))
    else:
        print("500kr bills: " + str(0))
    change = change % 500

    bill = change // 200
    if bill > 0:
        print("200kr bills: " + str(bill))
    else:
        print("200kr bills: " + str(0))
    change = change % 200
    
    bill = change // 100
    if bill > 0:
        print("100kr bills: " + str(bill))
    else:
        print("100kr bills: " + str(0))
    change = change % 100
    
    bill = change // 50
    if bill > 0:
        print("50kr bills: " + str(bill))
    else:
        print("50kr bills: " + str(0))
    change = change % 50
    
    bill = change // 20
    if bill > 0:
        print("20kr bills: " + str(bill))
    else:
        print("20kr bills: " + str(0))
    change = change % 20
    
    bill = change // 10
    if bill > 0:
        print("10kr bills: " + str(bill))
    else:
        print("10kr bills: " + str(0))
    change = change % 10
    
    bill = change // 5
    if bill > 0:
        print("5kr bills: " + str(bill))
    else:
        print("5kr bills: " + str(0))
    change = change % 5
    
    bill = change // 2
    if bill > 0:
        print("2kr bills: " + str(bill))
    else:
        print("2kr bills: " + str(0))
    change = change % 2
    
    bill = change // 1
    if bill > 0:
        print("1kr bills: " + str(bill))
    else:
        print("1kr bills: " + str(0))
    change = change % 1