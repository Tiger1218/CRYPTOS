from pwn import *
sh = remote("35.208.182.172" , 6000)
g = int(sh.recvline()[3:])
p = int(sh.recvline()[3:])
c = int(sh.recvline()[16:])
# print(g,p,c)
def testlens():
    for i in range(30,90):
        sh.sendline(str(256 ** i).encode())
        # sh.recvline()
        # sh.wait(1)
        recv = (sh.recvline())
        print(i,recv)
        # if recv == 1:
        #     print(i)
        #     sh.close()
        #     return True
# testlens() # 64 位
master = 0
for i in range(63 , -1 , -1):
    sh.sendline(str(256 ** i).encode())
    recv = sh.recvline()
    # print(recv,int(recv[18:]))
    recv = int(recv[18:])
    # print(recv)
    for k in range(256):
        if pow(g , master * 256 + k , p) == recv:
            master = master * 256 + k
            print(chr(k) , end="")
            break
print("\n" + str(master))