

class AES:
    S = [
        [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    ]

    InvS = [
        [0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
        [0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
        [0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
        [0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
        [0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
        [0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
        [0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
        [0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b],
        [0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73],
        [0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e],
        [0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b],
        [0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4],
        [0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f],
        [0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef],
        [0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61],
        [0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d]
    ]
    Rc = [
        0x8d, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a,
        0x2f, 0x5e, 0xbc, 0x63, 0xc6, 0x97, 0x35, 0x6a, 0xd4, 0xb3, 0x7d, 0xfa, 0xef, 0xc5, 0x91, 0x39
    ]
    mix = [
        [2, 3, 1, 1],
        [1, 2, 3, 1],
        [1, 1, 2, 3],
        [3, 1, 1, 2]
    ]
    inverseMix = [
        [14, 11, 13, 9],
        [9, 14, 11, 13],
        [13, 9, 14, 11],
        [11, 13, 9, 14]
    ]
    K = ''
    M = ''
    Key = []
    State = []
    inverseState = []
    w0 = ''
    w1 = ''
    w2 = ''
    w3 = ''

    def getK(self):
        return self.K

    def setK(self, k):
        self.K = k

    def getW0(self):
        return self.w0

    def setW0(self, w0):
        self.w0 = w0

    def getW1(self):
        return self.w1

    def setW1(self, w1):
        self.w1 = w1

    def getW2(self):
        return self.w2

    def setW2(self, w2):
        self.w2 = w2

    def getW3(self):
        return self.w3

    def setW3(self, w3):
        self.w3 = w3

    def AES(self, k, m):
        self.K = k
        self.M = m
        pass

    def timeE(self, value):
        pass

    def timeB(self, value):
        pass

    def timeD(self, value):
        pass

    def time9(self, value):
        pass

    def inverseMixColumn(self, value):
        pass

    def HextoBin(self, value):
        result = bin(int(value, 16))[2:].upper()
        length = len(result)
        if length < 64:
            for i in range(64):
                result = '0' + result
        return result
        pass

    def DectoBin(self, value, k):
        result = "{0:b}".format(value).upper()
        length = len(result)
        if length < k:
            for i in range(k - length):
                result = '0' + result
        return result
        pass

    def BintoHex(self, bin, maxlength):
        result = hex(int(bin, 2)).upper().lstrip('0X')
        length = len(result)
        # print('result',result)
        if length < maxlength:
            for i in range(maxlength - length):
                result = '0' + result
        return result
        pass

    def DectoHex(self, value):
        result = hex(value).upper().lstrip('0X')
        if len(result) < 2:
            result = '0' + result
        return result

    def mapKeytoW(self, key):
        self.w0 = key[0:8]
        self.w1 = key[8:16]
        self.w2 = key[16:24]
        self.w3 = key[24:len(key)]
        pass

    def HextoDec(self, value):
        return int(value, 16)

    def RC(self, i):
        return self.DectoHex(self.Rc[i]) + '000000'

    def rotWord(self, value, k, x):
        result = ''
        result = value[k * x:len(value)] + value[0:k * x]
        return result

    def subByte(self, value, a):
        result = ''
        s = []
        for i in range(0,len(value), 2):
            if i + 2 <= len(value):
                s.append(value[i:i + 2])
        print(s)
        for i in range(len(s)):
            #print(self.DectoHex(a[self.HextoDec(str(s[i][0]))][self.HextoDec(str(s[i][1]))]))
            result = result + self.DectoHex(a[self.HextoDec(str(s[i][0]))][self.HextoDec(str(s[i][1]))])
        return result

    def xor(self, bin1, bin2):
        result = ''
        maximum = max(len(bin1), len(bin2))
        minimun = min(len(bin1), len(bin2))
        if maximum == len(bin1):
            for i in range(maximum - minimun):
                bin2 = '0' + bin2
        else:
            for i in range(maximum - minimun):
                bin1 = '0' + bin1
        for i in range(maximum):
            result = result + str(int(str(bin1[i])) ^ int(str(bin2[i])))
        return result

    def shilfRows(self, value):
        result = ''
        list = []
        #print('value: ', value)
        for i in range(0,len(value), 2):
            if i + 2 <= len(value):
                list.append(value[i:i + 2])
        #print('list',list)
        row1 = ''
        row2 = ''
        row3 = ''
        row4 = ''
        for i in range(len(list)):
            if i % 4 == 0:
                row1 += list[i]
            elif i % 4 == 1:
                row2 += list[i]
            elif i % 4 == 2:
                row3 += list[i]
            else:
                row4 += list[i]
        row2 = self.rotWord(row2, 1, 2)
        row3 = self.rotWord(row3, 2, 2)
        row4 = self.rotWord(row4, 3, 2)
        for i in range(0,len(row1), 2):
            result += row1[i:i + 2] + row2[i:i + 2] + row3[i:i + 2] + row4[i:i + 2]
        #print("result",result)
        return result

    def setUpKey(self, key):
        #print(key)
        self.mapKeytoW(key)
        self.Key.append(self.w0 + self.w1 + self.w2 + self.w3)
        for i in range(10):
            #print('w3: ',self.w3)
            after_rot_word = self.rotWord(self.w3, 1, 2)
            print("After RotWord: " + after_rot_word)
            after_sub_bytes = self.subByte(after_rot_word, self.S)
            print("After SubBytes: " + after_sub_bytes)
            rc = self.RC(i + 1)
            print("Rc: " + rc)
            rc_xor_after = self.xor(self.HextoBin(rc), self.HextoBin(after_sub_bytes))
            print("rc xor after: " + self.BintoHex(rc_xor_after, 8))
            w4 = self.xor(self.HextoBin(self.w0), rc_xor_after)
            w5 = self.xor(self.HextoBin(self.w1), w4)
            w6 = self.xor(self.HextoBin(self.w2), w5)
            w7 = self.xor(self.HextoBin(self.w3), w6)
            self.w0 = self.BintoHex(w4, 8)
            self.w1 = self.BintoHex(w5, 8)
            self.w2 = self.BintoHex(w6, 8)
            self.w3 = self.BintoHex(w7, 8)
            self.Key.append(self.w0 + self.w1 + self.w2 + self.w3)

    def mixColumn(self, value):
        result = ""
        #print('value',value)
        row = []
        for i in range(0, 32, 2):
            if i+2 <= len(value):
                row.append(value[i: i + 2])
        #print("row",row)
        for i in range(4):
            for j in range(0, 16, 4):
                v1 = ""
                v2 = ""
                v3 = ""
                v4 = ""
                if self.mix[i][0] == 1:
                    v1 = self.HextoBin(row[j + 0])
                elif self.mix[i][0] == 2:
                    v1 = self.HextoBin(row[j + 0]) + "0"
                elif self.mix[i][0] == 3:
                    v1 = self.xor(self.HextoBin(row[j + 0]), self.HextoBin(row[j + 0]) + "0")
                if self.mix[i][1] == 1:
                    v2 = self.HextoBin(row[j + 1])
                elif self.mix[i][1] == 2:
                    v2 = self.HextoBin(row[j + 1]) + "0"
                elif self.mix[i][1] == 3:
                    v2 = self.xor(self.HextoBin(row[j + 1]), self.HextoBin(row[j + 1]) + "0")

                if self.mix[i][2] == 1:
                    v3 = self.HextoBin(row[j + 2])
                elif self.mix[i][2] == 2:
                    v3 = self.HextoBin(row[j + 2]) + "0"
                elif self.mix[i][2] == 3:
                    v3 = self.xor(self.HextoBin(row[j + 2]), self.HextoBin(row[j + 2]) + "0")

                if self.mix[i][3] == 1:
                    v4 = self.HextoBin(row[j + 3])
                elif self.mix[i][3] == 2:
                    v4 = self.HextoBin(row[j + 3]) + "0"
                elif self.mix[i][3] == 3:
                    v4 = self.xor(self.HextoBin(row[j + 3]), self.HextoBin(row[j + 3]) + "0")

                if self.checkGF(v1,0) == False:
                    v1 = self.xor(v1, "100011011")
                    v1 = self.And(v1, "11111111")

                if self.checkGF(v2,0) == False:
                    v2 = self.xor(v2, "100011011")
                    v2 = self.And(v2, "11111111")

                if self.checkGF(v3,0) == False:
                    v3 = self.xor(v3, "100011011")
                    v3 = self.And(v3, "11111111")

                if self.checkGF(v4,0) == False:
                    v4 = self.xor(v4, "100011011")
                    v4 = self.And(v4, "11111111")

                result += self.BintoHex(self.xor(self.xor(self.xor(v1, v2), v3), v4), 2)
        list = []

        for i in range(0, len(result), 2):
            if i + 2 <= len(result):
                list.append(result[i: i + 2])
        #print('list',list)
        row1 = ""
        row2 = ""
        row3 = ""
        row4 = ""

        for i in range(len(list)):
            if i % 4 == 0:
                row1 += list[i]

            elif i % 4 == 1:
                row2 += list[i]

            elif i % 4 == 2:
                row3 += list[i]

            else:
                row4 += list[i]

        #print("row:", row1 + row2 + row3 + row4)
        return row1 + row2 + row3 + row4

    def checkGF(self, value, k):
        i = 0

        for i in range(len(value)):
            if value[i] != '0':
                break
        value1 = value[i:len(value)]

        if len(value1) > 9 + k:
            return False
        elif len(value1) < 9 + k:
            return True

        else:
            for j in range(len(value1)-1,0,-1):
                if value1[j] != '0':
                    return False
        return True
        pass

    def And(self,bin1,bin2):
        result = ''
        maximun = max(len(bin1), len(bin2))
        minimum = min(len(bin1), len(bin2))
        if maximun == len(bin1):
            for i in range(maximun - minimum):
                bin2 = '0' + bin2
        else:
            for i in range(maximun - minimum):
                bin1 = '0' + bin1
        for i in range(maximun):
            result = result + str(int(str(bin1[i])) & int(str(bin2[i])))
        return result
        pass
    def encrypt(self):
        self.State.append(self.xor(self.HextoBin(self.K), self.HextoBin(self.M)))
        for i in range(1,10):
            afterSubBytes = self.subByte(self.BintoHex(self.State[i-1], 32), self.S)
            print("Subbyte: "+afterSubBytes)
            afterShilfRows = self.shilfRows(afterSubBytes)
            print("After shilfrow: "+afterShilfRows)
            mix = self.mixColumn(afterShilfRows)
            print("mix: "+mix)
            self.State.append(self.xor(self.HextoBin(self.Key[i]), self.HextoBin(mix)))
        afterSubBytes = self.subByte(self.BintoHex(self.State[9], 32), self.S)
        afterShilfRows = self.shilfRows(afterSubBytes)
        self.State.append(self.xor(self.HextoBin(self.Key[10]), self.HextoBin(afterShilfRows)))
        return self.BintoHex(self.State[len(self.State) - 1], 32)
if __name__ == '__main__':
    aes = AES()
    aes1 = aes.AES("2B7E151628AED2A6ABF7158809CF4F3C", "3243F6A8885A308D313198A2E0370734")
    aes.setUpKey(aes.getK())
    for i in range(len(aes.Key)):
        print(str(i)+"-->"+aes.Key[i])
    en = aes.encrypt()
    print("En----> " + en)
