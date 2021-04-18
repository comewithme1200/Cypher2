import math
def isPrime(n):
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2  == 0:
        return False
    for i in range(3,math.sqrt(n),2):
        if n % i == 0:
            return False
    return True