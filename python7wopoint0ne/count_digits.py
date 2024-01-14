n = input("Enter a large positive integer: ")
x = 0
is_even = 0
is_odd = 0
is_zero = 0
for i in n:
    y = int(i)
    if (y % 2 == 0) and y == 0:
        is_even += 1
    elif(y % 2 != 0):
        is_odd += 1
    else:
        is_zero += 1
        
print(f"Zeros: {is_zero}\nOdd: {is_odd}\nEven: {is_even}")