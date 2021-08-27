# -*-coding:utf-8-*-
import gmpy
import binascii
from flag import generateN,flag

assert(flag[:5] == "flag{")
assert(flag[-1] == "}")
ns = generateN()
cs = [0]*4
flag = flag[5:-1]
for i in range(4):
	tmp = flag[i*6:i*6+6]
	tmp = int(binascii.hexlify(tmp), 16)
	assert(cs[i] == pow(tmp, ns[i], ns[i]))
	cs.append(pow(tmp,ns[i],ns[i]))
f = open("output.txt")
f.write(ns,cs)
f.close()