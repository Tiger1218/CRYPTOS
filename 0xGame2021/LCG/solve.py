from Crypto.Util.number import GCD,inverse
from pwn import *
from functools import reduce
context(log_level = "debug")
def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment
def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * inverse(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)
def crack_unknown_modulus(states):
    diffs = [s1 - s0 for s0, s1 in zip(states, states[1:])]
    zeroes = [t2*t0 - t1*t1 for t0, t1, t2 in zip(diffs, diffs[1:], diffs[2:])]
    modulus = abs(reduce(GCD, zeroes))
    return crack_unknown_multiplier(states, modulus)
sh = remote("47.101.38.213", "60709")
breaks = []
for i in range(6):
    sh.recvuntil(b"> ")
    sh.sendline(b"1")
    sh.recvuntil(b"in decimal format>")
    sh.sendline(b"1")
    sh.recvuntil(b"Sorry,The Right Answer is")
    answer = sh.recvline()
    breaks.append(int(answer[:-1]))
    # log.info(f"GET NEW INFOS : {int(answer[:-1])}")

# log.info("GET ALL INFOS")

n , k , b = crack_unknown_modulus(breaks)
# log.info(f"n is {n} ; b is {b} ; k is {k}")
now = breaks[5]
# log.info(f"now is {now}")
for _ in range(200):
    sh.recvuntil(b"> ")
    sh.sendline(b"1")
    sh.sendline(str((k * now + b) % n).encode())
    # log.info(f"NEXT IS {str((k * now + b) % n)}")
    now = (k * now + b) % n