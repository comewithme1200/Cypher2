def power(x, y, p):
    res = 1
    x = x % p
    if x == 0:
        return 0
    while y > 0:
        if (y & 1) != 0:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


if __name__ == '__main__':
    print(power(11, 13, 19))