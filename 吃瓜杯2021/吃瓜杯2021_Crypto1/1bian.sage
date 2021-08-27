from Crypto.Util.number import *

n = 8870619487339789349033932217513908953609539651949986489986889710933094577873155191810742828503059670650154455297603719
e = 3

with open('flag.txt', 'rb') as f:
    m = bytes_to_long(f.read())

assert n > m

Zn = Zmod(n)
P = PermutationGroupElement('(1,6)(2,3,5)(4,7)')
P = Matrix(Zn, P.matrix())

def encrypt(m):
    C = (m * P) ^ e
    return C.list()