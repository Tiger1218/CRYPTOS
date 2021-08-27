from Crypto.Util.number import getPrime, long_to_bytes
from pwn import *
import random, binascii

flag = open('flag.txt').read()

def v(p, k):
	ans = 0
	while k % p == 0:
		k /= p
		ans += 1
	return ans

p, q, r = getPrime(2048), getPrime(2048), getPrime(2048)
print(p, q, r)
n = pow(p, q - 1) * p * r
phi_n = pow(p , q - 1) * (r - 1)

a1 = random.randint(0, n)
a2 = n - a1
assert a1 % p != 0 and a2 % p != 0

t = pow(a1, n) + pow(a2, n)

pow(a1 , phi_n , n) = 1
pow(a1 , )
print(binascii.hexlify(xor(flag, long_to_bytes(v(p, t)))))



