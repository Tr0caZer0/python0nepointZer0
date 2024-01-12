print("Please provide three integers A, B, C.")
a = int(input("Enter A: "))
b = int(input("Enter B: "))
c = int(input("Enter C: "))

if((a > b) and (a > c)):
    print("A: " + str(a) +  " is the largest")
elif((b > a) and (b > c)):
    print("B: " + str(b) +  " is the largest")
else:
    print("C: " + str(c) +  " is the largest")