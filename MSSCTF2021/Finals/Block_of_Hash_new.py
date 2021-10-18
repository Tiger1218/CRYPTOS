from Crypto.Util.number import*
from hashlib import sha256
import socketserver
import signal
import string
import random
from secret import flag
from Crypto.Cipher import AES
from binascii import hexlify
table = string.ascii_letters+string.digits

HashKey = b'welcometomssctf!'
def pad(m):
    padlen = 16 - len(m) % 16
    return m + padlen * bytes([padlen])

MENU = br'''
<OPTION>
'''

BLANK = br'''
 ______   __                 __                         ___           ____  ____                __       
|_   _ \ [  |               [  |  _                   .' ..]         |_   ||   _|              [  |      
  | |_) | | |  .--.   .---.  | | / ]          .--.   _| |_             | |__| |   ,--.   .--.   | |--.   
  |  __'. | |/ .'`\ \/ /'`\] | '' <         / .'`\ \'-| |-'            |  __  |  `'_\ : ( (`\]  | .-. |  
 _| |__) || || \__. || \__.  | |`\ \        | \__. |  | |             _| |  | |_ // | |, `'.'.  | | | |  
|_______/[___]'.__.' '.___.'[__|  \_]        '.__.'  [___]           |____||____|\'-;__/[\__) )[___]|__] 
                                                                                           
## ################  wow #### The #### Block_of_Hash #### has #### just #### began  ################ ##
'''
class Task(socketserver.BaseRequestHandler):
    def _recvall(self):
        BUFF_SIZE = 2048
        data = b''
        while True:
            part = self.request.recv(BUFF_SIZE)
            data += part
            if len(part) < BUFF_SIZE:
                break
        return data.strip()

    def send(self, msg, newline=True):
        try:
            if newline:
                msg += b'\n'
            self.request.sendall(msg)
        except:
            pass

    def recv(self, prompt=b'SERVER <INPUT>: '):
        self.send(prompt, newline=False)
        return self._recvall()

    def MyHash(self, m):
        aes = AES.new(HashKey , AES.MODE_CBC , iv = HashKey)
        return aes.encrypt(m)[-16:]


    def proof_of_work(self):
        proof = (''.join([random.choice(table)for _ in range(16)])).encode()
        sha = self.MyHash(proof)
        self.send(b"[+] sha256(XXX+" + proof[3:] + b") == " + hexlify(sha))
        XXX = self.recv(prompt = b'[+] Plz Tell Me XXX :')
        if len(XXX) != 3 or self.MyHash(XXX + proof[3:]) != sha:
            return False
        return sha
    
        
    def transaction_hash_generator(self,hashes,transaction):
        block = pad(transaction) + hashes
        return self.MyHash(block)

    def Pr0of_oF_w00k(self,hashes,limited,transaction):
        nonce = random.randrange(0,limited)
        proof = pad(transaction + hex(nonce)[2:].encode()) + hashes
        sha = self.MyHash(proof)
        return sha

    def handle(self):
        
        FirstBlockHash = self.proof_of_work()
        if not FirstBlockHash:
            return
        signal.alarm(180)
        self.send(BLANK)
        for _ in range(5):
            transaction = b"0x114514 transfer 1 bitcoin to 0x1919810"
            BlockHash = self.transaction_hash_generator(FirstBlockHash,transaction)

            limited = 2**11
            self.send(b"SERVER <OUTPUT>:" + str(limited).encode())
            for i in range(3):
                BlockHash = self.Pr0of_oF_w00k(BlockHash,limited,transaction)
            BlockHash = hexlify(BlockHash)
            self.send(b"SERVER <OUTPUT>:Do you already compute the hash? I will give you some hint:" + BlockHash[:29])
            guess = self.recv()
            if guess == BlockHash:
                self.send(b"SERVER <OUTPUT>:Oh you are true")
            else:
                self.send(b"SERVER <OUTPUT>:you Lose!    :(")
                break
        else:
            self.send(b"SERVER <OUTPUT>:flag is " + flag + b'  :)' )
                
        self.send(b"\nConnection has been closed  =.=  ")
        self.request.close()


class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10001
    print("HOST:POST " + HOST+":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()