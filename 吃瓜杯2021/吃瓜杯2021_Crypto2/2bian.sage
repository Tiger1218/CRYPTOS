from Crypto.Util.number import *
import random
random.seed(0x36D)

n = 3950848271664122675439855009329233027357977239695163232943132810210035583520735079984423511153607529820284200137188647
e = 3

with open('flag.txt', 'rb') as f:
    m = bytes_to_long(f.read())

assert n > m

Zn = Zmod(n)
P = PermutationGroupElement('(1,14,25,8,23,15)(2,22,17)(3,18,13,33,11,30,26,27,10,6,16,31,28,21,29,36,7,9)(4,35,12,32,20,5,24)(19,34)')
P = Matrix(Zn, P.matrix())
A = Matrix(Zn, 36, 36, lambda x, y: random.randint(0, 0x36D))
B = A * P * A^-1 # B * A = A * P

def encrypt(m):
    C = (m * B) ^ e
    return C.list()