import PhiEuler
import DownGradedModulo


def isCamNT(a, n):
    phiN = PhiEuler.phi(n)
    if DownGradedModulo.power(a, phiN, n) == 1:
        for i in range(phiN):
            if phiN % i == 0:
                if (DownGradedModulo.power(a, i, n)):
                    return False
        return True
    return False
if __name__ == '__main__':
    print(isCamNT(10,5))