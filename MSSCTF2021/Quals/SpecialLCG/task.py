from Crypto.Util.number import*

flag = xxxxxxxxxxxxxxxxxxxxxxxx
assert(len(flag) == 24)

class LCG:
    def __init__(self, seed1 , seed2):
        self.seed1 = seed1
        self.seed2 = seed2
        self.state = [seed1,seed2]
        self.n = getPrime(64)
        while 1:
            self.a = bytes_to_long(flag[:8])
            self.b = bytes_to_long(flag[8:16])
            self.c = bytes_to_long(flag[16:])
            if self.a < self.n and self.b < self.n and self.c < self.n:
                break
        print("n = " + str(self.n))
    
    def next(self):
        new = (self.a * self.state[-1] + self.b * self.state[-2] + self.c) % self.n
        self.state.append( new )
        return new

def main():
    seed1 = getRandomInteger(64)
    seed2 = getRandomInteger(64)
    lcg = LCG(seed1 , seed2)
    data = []
    for i in range(5):
        data.append(lcg.next())
    print("data = " + str(data))

if __name__ == "__main__":
    main()

'''
output:

n = 18253588106473969889
data = [8331802587873314500, 16970700310063771377, 16378474859328460142, 13073117282614811463, 747433301416436433]
'''