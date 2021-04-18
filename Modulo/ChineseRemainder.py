import InverseModulo


def chineseremainder(a, m, n):
    M = 1
    for i in range(n):
        M = M * m[i]
    sum = 0
    for i in range(n):
        sum = sum + a[i] * (M / m[i]) * InverseModulo.inverse_modulo(M / m[i], m[i])
    return int(sum % M)


if __name__ == '__main__':

    pass
    # print(chineseremainder(13,11,19))
