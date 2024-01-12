import math

radius = float(input("Provide radius: "))

sphere = round(((pow(radius,3)*math.pi)*4)/3, 1)

print("volume of the sphere is " + str(sphere))