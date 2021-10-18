from Crypto.Util.number import*
from hashlib import sha256
import socketserver
import signal
import string  
import random
from secret import flag

table = string.ascii_letters+string.digits

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

    def proof_of_work(self):
        proof = (''.join([random.choice(table)for _ in range(20)])).encode()
        sha = sha256(proof).hexdigest().encode()
        self.send(b"[+] sha256(XXXX+" + proof[4:] + b") == " + sha )
        XXXX = self.recv(prompt = b'[+] Plz Tell Me XXXX :')
        if len(XXXX) != 4 or sha256(XXXX + proof[4:]).hexdigest().encode() != sha:
            return False
        return sha.decode()

    def transaction_hash_generator(self,hashes,transaction):
        block = long_to_bytes(int(hashes,16)) + transaction
        return sha256(block).hexdigest().encode()

    def Pr0of_oF_w00k(self,hashes,limited,transaction):
        nonce = random.randrange(0,limited)
        proof = hashes + str(nonce).encode() + transaction
        sha = sha256(proof).hexdigest().encode()
        return sha

    def handle(self):
        signal.alarm(20)
        FirstBlockHash = self.proof_of_work()
        if not FirstBlockHash:
            return

        self.send(BLANK)
        transaction = b"0x114514 transfer 1 bitcoin to 0x1919810"
        BlockHash = self.transaction_hash_generator(FirstBlockHash,transaction)

        limited = random.randrange(0,2**10)
        self.send(b"SERVER <OUTPUT>:" + str(limited).encode())
        for i in range(3):
            BlockHash = self.Pr0of_oF_w00k(BlockHash,limited,transaction)
            limited = limited//2

        self.send(b"SERVER <OUTPUT>:Do you already compute the hash? I will give you some hint:" + BlockHash[:8])
        guess = self.recv()
        if guess == BlockHash:
            self.send(b"SERVER <OUTPUT>:flag is " + flag + b'  :)' )
        else:
            self.send(b"SERVER <OUTPUT>:you Lose!    :(")
        self.send(b"\nConnection has been closed  =.=  ")
        self.request.close()

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10011
    print("HOST:POST " + HOST+":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()