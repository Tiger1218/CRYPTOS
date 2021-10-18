from pwn import *
from hashlib import sha256
import string
context.log_level = "debug"
table = string.ascii_letters+string.digits
sh = remote("81.68.112.139","10005")
def bypass_POF():
    raw = sh.recvline()
    paddings, outputs = raw[15:15 + 9] , raw[29:29+64]
    # print(paddings,outputs)
    for i in table:
        for j in table:
            for k in table:
                if sha256((i + j + k).encode() + paddings).hexdigest().encode() == outputs:
                    sh.sendline((i + j + k).encode())
    sh.interactive()
bypass_POF()