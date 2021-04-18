def inverse_modulo(a, n):
    for i in range(1, n):
        if (a * i) % n == 1:
            return i
    return -1
if __name__ == '__main__':
    print(inverse_modulo(6,13))