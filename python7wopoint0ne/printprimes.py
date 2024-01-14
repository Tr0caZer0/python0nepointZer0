def checkForPrime(number):
    for i in range(2, int(number**0.5) + 1):
        if(number % i == 0):
            return False
    return True
primes = int(input("How many primes? "))

myPrimeString = ""
primesAdded = 0
count = 0
for i in range(2, primes *10):
    if(checkForPrime(i)):
        count += 1
        if(count < primes+1):
            myPrimeString += str(i) + " "
            primesAdded += 1
                
            if primesAdded % 10 == 0:
                myPrimeString += "\n"
print(myPrimeString)