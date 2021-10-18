#!/usr/bin/python
from Crypto.Util.number import *
import random
import gmpy2
from secret import flag

def generateKey(bitlen):
    u = 2
    v = 200
    seed = random.randint(3**bitlen,4**bitlen)
    sequence = [seed]
    s = seed
    for i in range(1,bitlen):
        seed = random.randint(s + v, u*(s+v))
        sequence.append(seed)
        s += seed
    q = random.randint(s+v, u*(s+v))
    r = random.randint(1, q)
    while gmpy2.gcd(r, q) != 1:
        r = random.randint(1, q)
    key = [ r*w % q for w in sequence]
    return key


def encrypt(msg, pubKey):
	msg_bit = msg
	n = len(pubKey)
	cipher = 0
	i = 0
	for bit in msg_bit:
		cipher += int(bit)*pubKey[i]
		i += 1
	return bin(cipher)[2:]

msg = bin(bytes_to_long(flag))[2:]
key = generateKey(len(msg))
enc =  encrypt(msg, key)
print key
print int(enc, 2)


