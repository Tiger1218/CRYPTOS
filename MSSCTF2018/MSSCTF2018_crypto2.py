from Crypto.Random import random
from Crypto.PublicKey import DSA
from Crypto.Hash import SHA
from Crypto.Util.number import bytes_to_long
import time

message = b"w31c0me_t0_x1dian_univers1ty_0erferwj3"
key = DSA.generate(1024)
h = SHA.new(message).digest()
print(bytes_to_long(h))
# k = int(time.time())
# sig = key.sign(h,k)

# print(key.p)
# print(key.q)
# print(key.g)
# print(sig)

# flag = str(key.sign(h[::-1], k)[1])

# print(flag)