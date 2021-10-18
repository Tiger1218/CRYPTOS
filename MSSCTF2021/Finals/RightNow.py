from Crypto.Util.number import*
from secret import flag
import random

assert flag[:7] == b'mssctf{' and flag[-1:] == b'}'
assert len(flag) == 32
class Random_number_Generator:
    def __init__(self,seed):
        self.state = seed
    
    def next(self):
        shift = self.state >> 16
        self.state = self.state ^ shift
        return self.state

m = bytes_to_long(flag[7:-1])

while 1:
    salt = random.getrandbits(192)
    if  len(bin(salt)) == 194:
        break

prng = Random_number_Generator((salt))
print(prng.next())

c = salt ^ m
print(c)
'''
output :
5673455472531000341336769521901655216882120337947867201737
4445782886082916185056383186591673482419388050169044634898
'''