from sage.all import *
from Crypto.Util.number import *
from secret import flag

def _N2M_(num,wid):
    mat = []
    num = bin(num)[2:].rjust(wid*wid,'0')
    for i in range(wid):
        TMP = []
        for j in range(wid):
            TMP.append(int(num[i*wid + j]))
        mat.append(TMP)
    return mat

def _T_(mat,wid):
    new_mat = []
    for i in range(wid):
        TMP = []
        for j in range(wid):
            TMP.append(int(mat[j][i]))
        new_mat.append(TMP)
    return new_mat

def _GenKeyM_(wid):
    Prime_bits = 256
    primes = [[getPrime(Prime_bits) for i in range(wid)] for j in range(wid)]
    return primes

if __name__ == "__main__":
    wid = 17
    m = bytes_to_long(flag)
    m = _T_(_N2M_(m,wid),wid)

    m = Matrix(ZZ,m)
    key = _GenKeyM_(wid)

    c = m * Matrix(ZZ,key)
    f = open(r'/output','w')

    bigMOD = 2**512
    A = 0x10001
    B = 12138
    KEY = A * Matrix(Zmod(bigMOD),key) + B

    f.write("cipher : \n" + str(c) + '\nKEY :\n' + str(KEY))
    f.close()
