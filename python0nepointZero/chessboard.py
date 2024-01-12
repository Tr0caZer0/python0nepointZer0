import re
chessSquareColor = str(input("Enter a chess square identifier (e.g. e5): "))

match = re.match(r"([a-zA-Z]+)(\d+)", chessSquareColor)

getChar = ""
getInt = 0

if(match):
    getChar = match.group(1)
    getInt = match.group(2)

print("char: " + getChar + ", int: " + str(getInt))

if((int(getInt) % 2) != 0):#ODD
    if(getChar in ["a", "c", "e", "g"]):
        print(chessSquareColor + " is black")
    else:
        print(chessSquareColor + " is white") 
else:
    if(getChar in ["b", "d", "f", "h"]):
        print(chessSquareColor + " is black")
    else:
        print(chessSquareColor + " is white") 
    

# 32 balck
# 32 white
# a black odd
# b black even
# c black odd
# d black even
# e black odd
# f black even
# g black odd
# h black even