import coPrime
import PhiEuler
import DownGradedModulo


def euler(a, b, n):
    b1 = 0
    soA = 0
    if coPrime.coprime(a, n):
        b1 = b % PhiEuler.phi(n)
        return DownGradedModulo.power(a, b1, n)
    else:
        soA = int(b / (PhiEuler.phi(n) + 1))
        b1 = (b % (PhiEuler.phi(n) + 1)) + soA
        return DownGradedModulo.power(a, b1, n)

if __name__ == '__main__':
    print(euler(13,11,19))