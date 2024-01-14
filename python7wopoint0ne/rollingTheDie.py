import random

# 1-6 die
# 20 roll turnes 
# Doubeling the roles each turn. 10, 20, 40, 80 and so on.... 
# Calc the difference between the face that shows up the most times and the one least time. 2/8 to get persantage. 

roles = 10

for y in range(20):
    if y >= 1:
        roles *= 2
    faceOne = 0
    faceTwo = 0
    faceThree = 0
    faceFour = 0
    faceFive = 0
    faceSix = 0
    for i in range(1,roles + 1):
        
        die = random.randint(1,6)
        if die == 1:
            faceOne += 1
        elif die == 2:
            faceTwo += 1
        elif die == 3:
            faceThree += 1
        elif die == 4:
            faceFour += 1
        elif die == 5:
            faceFive += 1
        elif die == 6:
            faceSix += 1
    
    dieFace = [faceOne, faceTwo, faceThree, faceFour, faceFive, faceSix]
    largestFace = (max(dieFace))
    smallestFace = (min(dieFace))
    if largestFace == 0:
        difference = 100  # Avoid division by zero error
    else:
        difference = round(float((largestFace - smallestFace) / largestFace) * 100,2)
    print("For " + str(roles) + ", the difference is " + str(difference) + "%")
    
    
    
# For 10 rolls, the difference is 100.0%



