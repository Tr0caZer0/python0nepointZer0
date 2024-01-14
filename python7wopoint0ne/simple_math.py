def inc(n):          
    n += 1
    return n

def inc_with(n, t):   
    n += t
    return n

def dec(n):
    n -= 1
    return n
    
def dec_with(n, t):
    n -= t
    return n

def greatest(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
    
def power(x, n):
    return x**n

def factorial(n):
    x = 1
    if n > 0:
        for i in range(n, 0, -1):
            x *= i
            
            
    else:
        return 1
    return x

print('41 plus 1:', inc(41))
print('30 plus 12:', inc_with(30, 12))

print('43 minus 1:', dec(43))
print('52 minus 10:', dec_with(52, 10))

print('Which is greater, 24 or 42?', greatest(24, 42))

print('Is 42 even?: ', is_even(42))

print('2 to the power of 16:', power(2, 16))

print('Factorial of 5:', factorial(5))