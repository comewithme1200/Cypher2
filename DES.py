from array import *
import binascii


class DES:
    s = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

    PC1 = [
        [57, 49, 41, 33, 25, 17, 9, 1],
        [58, 50, 42, 34, 26, 18, 10, 2],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [60, 52, 44, 36, 63, 55, 47, 39],
        [31, 23, 15, 7, 62, 54, 46, 38],
        [30, 22, 14, 6, 61, 53, 45, 37],
        [29, 21, 13, 5, 28, 20, 12, 4]
    ]
    PC2 = [
        [14, 17, 11, 24, 1, 5],
        [3, 28, 15, 6, 21, 10],
        [23, 19, 12, 4, 26, 8],
        [16, 7, 27, 20, 13, 2],
        [41, 52, 31, 37, 47, 55],
        [30, 40, 51, 45, 33, 48],
        [44, 49, 39, 56, 34, 53],
        [46, 42, 50, 36, 29, 32]
    ]
    IP = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
    ]
    IP_1 = [
        [40, 8, 48, 16, 56, 24, 64, 32],
        [39, 7, 47, 15, 55, 23, 63, 31],
        [38, 6, 46, 14, 54, 22, 62, 30],
        [37, 5, 45, 13, 53, 21, 61, 29],
        [36, 4, 44, 12, 52, 20, 60, 28],
        [35, 3, 43, 11, 51, 19, 59, 27],
        [34, 2, 42, 10, 50, 18, 58, 26],
        [33, 1, 41, 9, 49, 17, 57, 25]
    ]
    E = [
        [32, 1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8, 9],
        [8, 9, 10, 11, 12, 13],
        [12, 13, 14, 15, 16, 17],
        [16, 17, 18, 19, 20, 21],
        [20, 21, 22, 23, 24, 25],
        [24, 25, 26, 27, 28, 29],
        [28, 29, 30, 31, 32, 1]
    ]
    S = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
        ],
    ]
    P = [
        [16, 7, 20, 21],
        [29, 12, 28, 17],
        [1, 15, 23, 26],
        [5, 18, 31, 10],
        [2, 8, 24, 14],
        [32, 27, 3, 9],
        [19, 13, 30, 6],
        [22, 11, 4, 25]
    ]
    C = []
    D = []
    Key = []
    L = []
    R = []
    LD = []
    RD = []
    K = ''
    M = ''

    def DES(self,k, m):
        self.K = k
        self.M = m
        pass


    def HextoBin(self,value):
        result = bin(int(value, 16))[2:].upper()
        length = len(result)
        if length < 64:
            for i in range(64):
                result = '0' + result
        return result
        pass


    def DectoBin(self,value):
        result = "{0:b}".format(value).upper()
        length = len(result)
        if length < 4:
            for i in range(4 - length):
                result = '0' + result
        return result
        pass


    def BintoHex(self,bin):
        result = hex(int(bin, 2)).upper()
        return result
        pass


    def permutation(self,value, a):
        result = ''
        for i in range(len(a)):
            for j in range(len(a[i])):
                pass
                result = result + value[a[i][j] - 1]
        return result
        pass


    def rotLeftShift(self,value, number):
        left = value[0:number]
        right = value[number:len(value)]
        return right + left
        pass


    def setUpCD(self):
        result = self.permutation(self.HextoBin(self.K), self.PC1)
        self.C.append(result[0:28])
        self.D.append(result[28:len(result)])
        for i in range(len(self.s)):
            self.C.append(self.rotLeftShift(self.C[i], self.s[i]))
        for i in range(len(self.s)):
            self.D.append(self.rotLeftShift(self.D[i], self.s[i]))
        pass


    def setUpKey(self):
        for i in range(len(self.C) - 1):
            CD = self.C[i + 1] + self.D[i + 1]
            self.Key.append(self.permutation(CD, self.PC2))
        pass


    def setUpLR(self):
        IPM = self.permutation(self.HextoBin(self.M), self.IP)
        self.L.append(IPM[0:32])
        self.R.append(IPM[32:len(IPM)])
        for i in range(16):
            self.L.append(self.R[i])
            self.R.append(self.xor(self.functionF(self.R[i], self.Key[i]), self.L[i]))
        pass


    def xor(self,bin1, bin2):
        result = ""
        for i in range(len(bin1)):
            result = result + str(int(str(bin1[i])) ^ int(str(bin2[i])))
        return result
        pass


    def SBox(self,value):
        values = []
        for i in range(len(value)):
            if (i*6) + 6 <= len(value):
                values.append(value[i*6:(i*6) + 6])
            else:
                break
        result = ''
        i = 0
        for x in values:
            row = str(x[0]) + str(x[len(x) - 1])
            if '00' == row:
                result = result + self.DectoBin(self.S[i][0][int(x[1:5], 2)])
            elif '01' == row:
                result = result + self.DectoBin(self.S[i][1][int(x[1:5], 2)])
            elif '10' == row:
                result = result + self.DectoBin(self.S[i][2][int(x[1:5], 2)])
            else:
                result = result + self.DectoBin(self.S[i][3][int(x[1:5], 2)])
            i += 1
        return result
        pass


    def functionF(self,R, K):
        ER = self.permutation(R, self.E)
        Sbox = self.SBox(self.xor(ER, K))
        print("A=" + self.BintoHex(self.xor(R, K)) + " SBox: " + self.BintoHex(Sbox))
        PSB = self.permutation(Sbox, self.P)
        print("ER: " + self.BintoHex(ER) + " PSB: " + self.BintoHex(PSB))
        return PSB
        pass


    def encrypt(self):
        self.setUpCD()
        self.setUpKey()
        self.setUpLR()
        return self.permutation(self.R[len(self.R) - 1] + self.L[len(self.L) - 1], self.IP_1)
        pass


    def decrypt(self,cyphertext):
        IPD = self.permutation(self.HextoBin(cyphertext), self.IP)
        self.LD.append(IPD[0:32])
        self.RD.append(IPD[32:len(IPD)])
        for i in range(16):
            self.LD.append(self.RD[i])
            self.RD.append(self.xor(self.functionF(self.RD[i],self.Key[16-i-1]),self.LD[i]))
        return self.permutation(self.RD[len(self.RD)-1]+self.LD[len(self.LD)-1],self.IP_1)
        pass


if __name__ == '__main__':
    des = DES()
    des1 = des.DES("F7918DFD6815020C", "D8B8217DA16D5B5F")
    cyphertext = des.encrypt()
    print("Chuoi da ma hoa: " + des.BintoHex(cyphertext))
    print("Giai ma: " + des.BintoHex(des.decrypt(des.BintoHex(cyphertext))))
    print("Khoa: ")
    for i in range(len(des.Key)):
        print("K" + str(i) + " = " + des.BintoHex(des.Key[i]))
    print("L, R: ")
    for i in range(len(des.R)):
        print("L"+str(i)+" = "+des.BintoHex(des.L[i])+'\t'+"R"+str(i)+" = "+des.BintoHex(des.R[i]))


    pass

