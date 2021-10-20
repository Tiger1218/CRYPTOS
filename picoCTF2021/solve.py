from pwn import *
from Crypto.Cipher import DES
from Crypto.Util.number import *
from binascii import hexlify
import string
table = string.digits
sh = remote("mercury.picoctf.net" , "33425")
context(log_level = "debug")
sh.recvuntil(b"Here is the flag:\n")
flag = long_to_bytes(int(sh.recvline()[:-1], 16))
log.info(f"flag is {hexlify(flag)}")
sh.recvuntil(b"What data would you like to encrypt?")
sh.sendline(b"4141414141414141")
plaintext = 'AAAAAAAA'
ciphertext = long_to_bytes(int(sh.recvline()[:-1], 16))
log.info(f"Ciphertext is {hexlify(ciphertext)}")
def pad(msg):
    block_len = 8
    over = len(msg) % block_len
    pad = block_len - over
    return (msg + " " * pad).encode()
# sh.close()
plaintext = pad(plaintext)
mids = {}
for i in table:
    for j in table:
        for k in table:
            for l in table:
                for p in table:
                    for o in table:
                        key = pad(i + j + k + l + p + o)
                        # log.info(f"key is {key}")
                        des = DES.new(key , DES.MODE_ECB)
                        dec = des.decrypt(ciphertext)
                        mids.setdefault(dec , key)
log.info("ALL LOAD IN TABLE")
for i in table:
    for j in table:
        for k in table:
            for l in table:
                for p in table:
                    for o in table:
                        key = pad(i + j + k + l + p + o)
                        # log.info(f"key is {key}")
                        des = DES.new(key , DES.MODE_ECB)
                        enc = des.encrypt(plaintext)
                        if enc in mids:
                            # log.info(f"key1 is {key} , key2 is {mids[enc]} ; found")
                            des1 = DES.new(key , DES.MODE_ECB)
                            des2 = DES.new(mids[enc] , DES.MODE_ECB)
                            flag = des2.decrypt(flag)
                            flag = des1.decrypt(flag)
                            log.info(f"The flag is {(flag)}")
log.info("ALL SEARCH")