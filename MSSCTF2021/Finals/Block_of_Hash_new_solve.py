# from Crypto.Signature.pkcs1_15 import Hash
from cryptography.hazmat.primitives import ciphers
from pwn import *
from hashlib import *
from Crypto.Util.number import *
from Crypto.Cipher import AES
import string
theCiphers = []
transaction = b"0x114514 transfer 1 bitcoin to 0x1919810"
table = string.ascii_letters+string.digits
context(log_level = "debug")
HashKey = b'welcometomssctf!'
def Pr0of_oF_w00k(hashes,nonce):
    proof = pad(transaction + hex(nonce)[2:].encode()) + hashes
    sha = MyHash(proof)
    return sha
def pad(m):
    padlen = 16 - len(m) % 16
    return m + padlen * bytes([padlen]) # paddings
def MyHash(m):
    aes = AES.new(HashKey , AES.MODE_CBC , iv = HashKey)
    return aes.encrypt(m)[-16:]
def transaction_hash_generator(hashes,transaction):
    block = pad(transaction) + hashes
    return MyHash(block)
sh = remote("4c8a8626-a63b-4ac7-96c8-805dc2cbe536.mssctf.offline", 1443, ssl=True)
canary = sh.recvline()
proofs = canary[15 : 15 + 13].decode()
Hashs = canary[33 : 33 + 32].decode()
log.info(f"proofs is '{proofs}' and Hashs is '{Hashs}'")
for i in table:
    for j in table:
        for k in table:
            # print(type(MyHash((i + j + k + proofs).encode())),type(Hashs.encode()))
            if MyHash((i + j + k + proofs).encode()) == long_to_bytes(int(Hashs , 16)):
                log.info(f"proofs is {i + j + k}")
                sh.sendline((i + j + k).encode())
                # sh.interactive()
                # Meet In The Middle Attack
                
                # limits = 2 ** 11
                FirstBlockHash = long_to_bytes(int(Hashs , 16))
                for _ in range(5):
                    BlockHash = transaction_hash_generator(FirstBlockHash,transaction)
                    sh.recvuntil(b"SERVER <OUTPUT>:Do you already compute the hash? I will give you some hint:")
                    hints = int(sh.recvline()[:-1].decode() , 16)
                    # aes = AES.new(HashKey , AES.MODE_ECB)
                    # for k1 in range(2048):
                    #     p1 = Pr0of_oF_w00k(BlockHash , k1)
                    #     for k2 in range(1024):
                    #         theCiphers.append(Pr0of_oF_w00k(p1 , k2))
                    # blocksa = [b"0x114514 transfe" , b"r 1 bitcoin to 0" , b"x1919810"]
                    # iv1 = aes.encrypt(xor(blocksa[0] , HashKey))
                    # iv2 = aes.encrypt(xor(blocksa[1] , iv1))
                    # print(theCiphers)
                    # for k3 in range(512):
                    #     iv3 = aes.encrypt(xor(pad(blocksa[2] + hex(k3)[2:].encode()) , iv2))
                    #     for k4 in range(2 ** (3 * 4)):
                    #         if xor(aes.decrypt(pad(long_to_bytes(k4 * 2 ** (29 * 4) + (hints)))) , iv3) in theCiphers:
                    #             print(k3)
                # for _ in range(5):
                #     BlockHash = transaction_hash_generator(FirstBlockHash,transaction)
                #     sh.recvuntil(b"SERVER <OUTPUT>:Do you already compute the hash? I will give you some hint:")
                #     hints = int(sh.recvline()[:-1].decode() , 16)
                #     aes = AES.new(HashKey , AES.MODE_CBC , iv = HashKey)
                #     log.info(f"hints is {hex(hints)}")
                #     for front in range(2**12):
                #         for nonce in range(2 ** 9):
                #             realcipher = pad(transaction + hex(nonce)[2:].encode()) + long_to_bytes(front << (29 * 4) + hints).rjust(16 , b"\x00")
                #             theCiphers.append(aes.decrypt(realcipher)[-16:])
                #     # dfs(0 , BlockHash , hints , limits)
                #     # for k1 in range(2048):
                #     #     n1 = Pr0of_oF_w00k(BlockHash , k1)
                #     #     for k2 in range(1024):
                #     #         if Pr0of_oF_w00k(n1 , k2) in theCiphers:
                #     #             for k3 in range()
                sh.interactive()