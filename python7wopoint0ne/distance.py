import math

x1 = round(int(input("Enter x1: ")), 1)
y1 = round(int(input("Enter y1: ")), 1)
x2 = round(int(input("Enter x2: ")), 1)
y2 = round(int(input("Enter y2: ")), 1)

distance = round(math.sqrt(((x1-x2)**2) + ((y1-y2)**2)),3)

print(f"The distance between ({x1},{y1}) and ({x2},{y2}) is {distance}")