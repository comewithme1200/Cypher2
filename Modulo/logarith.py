import DownGradedModulo


def logarith(a, b, n):
    for i in range(n):
        if b == DownGradedModulo.power(a, i, n):
            return i
    return -1


if __name__ == '__main__':
    print(logarith(13, 11, 19))
