import math
def phi(n):
    result = 1
    for i in range(n-2):
        if math.gcd(i,n) == 1:
            result+=1
    return result
if __name__ == '__main__':
    print(phi(10))