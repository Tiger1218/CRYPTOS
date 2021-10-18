from Crypto.Util.number import *
from gmpy2 import invert
from secret import flag,e

def enc(key, p):
    e, n = key
    cipher = [pow(ord(char), e, n) for char in p]
    return cipher

def dec(pk, c):
    key, n = pk
    plain = [chr(pow(char, key, n)) for char in c]
    return ''.join(plain)

p = getPrime(512)
q = getPrime(512)
n = p*q
pubkey = (e,n)
assert(e < 20000)
print("Public key:")
print(pubkey[1])

cipher = (enc(pubkey, flag))

print("Encrypted flag:")
print(cipher)



