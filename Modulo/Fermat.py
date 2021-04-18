import isPrime
import  DownGradedModulo

def fermat(a, b, n):
    b1 = 0
    if isPrime.isPrime(n) and a > 0:
        b1 = b % (n - 1)
        return DownGradedModulo.power(a, b1, n)
    return -1

if __name__ == '__main__':
    pass
