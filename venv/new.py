def HextoBin(self, value):
    result = bin(int(value, 16))[2:].upper()
    length = len(result)
    if length < 64:
        for i in range(64):
            result = '0' + result
    return result
print(HextoBin())