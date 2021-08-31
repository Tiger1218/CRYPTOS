from Crypto.Cipher import AES
from hashlib import sha256
import socketserver
import signal
import string
import random

from secret import ivv,key,plaintext,flag

table = string.ascii_letters+string.digits

MENU = br'''
[+] 1.GetEncryptedData:
[+] 2.Hint:
[+] 3.Exit:
[+] 4.Check:
'''
BLANK = br'''
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
||      ____   _____       _______     _______     _______    ____________    ________        ||
||     |    \ |     \     /  ____/    /  ____/    /  _____\   \____   ____\   \   ____\       ||
||     |     \|      \    \  \_____   \  \_____   \  \             \  \        \  \_____      ||
||     |   |\    |\   \    \_____  \   \_____  \   \  \             \  \        \   ____\     ||
||     |   | \   | \   \    _____\  \   _____\  \   \  \______       \  \        \  \         ||
||     |__ |  \__|  \___\   \_______/   \_______/    \________\       \__\        \__\        ||
||                                                                                            ||
-=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=--=-
'''

def xor(msg1,msg2):
    assert len(msg1)==len(msg2)
    res = b''
    for i in range(len(msg1)):
        res += chr(msg1[i] ^ msg2[i]).encode()
    return res

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

    def recv(self, prompt=b'[-] '):
        self.send(prompt, newline=False)
        return self._recvall()

    def proof_of_work(self):
        proof = (''.join([random.choice(table)for _ in range(12)])).encode()
        sha = sha256( proof ).hexdigest().encode()
        self.send(b"[+] sha256(XXX+" + proof[3:] + b") == " + sha )
        XXX = self.recv(prompt = b'[+] Plz Tell Me XXX :')
        if len(XXX) != 3 or sha256(XXX + proof[3:]).hexdigest().encode() != sha:
            return False
        return True

    def Enc(self):
        iv = ivv
        self.salt = b'I_am_just_a_salt'
        self.plain = self.salt + plaintext
        aes = AES.new(key,AES.MODE_CBC,iv)
        self.cipher = aes.encrypt(self.plain)
        return self.cipher , xor( self.salt , key )

    def Hint(self):
        aes = AES.new(key,AES.MODE_CBC,self.cipher[:16])
        return aes.decrypt(self.cipher[16:])

    def Check(self):
        msg = self.recv(prompt = b'[-] ivv is:\n')
        if msg == ivv:
            self.send(b"Ohhhhh!Correct!")
            self.send(b"flag: " + flag)
            return True
        else:
            self.send(b"[!] WRONG.Plz dec again!")
            return False


    def handle(self):
        signal.alarm(50)
        if not self.proof_of_work():
            return
        self.send(BLANK)
        self.send(b'\\\\\\\\~~~~~~=====================||||Welcome to MSSCTF 2021!||||=======================~~~~~~////')
        self.send(b'\\\\\\\\\\__________________________||||Do U Know CBC and ECB? ||||____________________________/////')

        while 1:
            self.send(MENU,newline = False)
            option = self.recv()
            if (option == b'1'):
                c , x = self.Enc()
                self.send(b'[+] cipher :' + c,newline = False)
                self.send(b'[+] xor(salt,key) :' + x)
            elif option == b'2':
                hint = self.Hint()
                self.send(b'[+] HINT :' + hint)
            elif option == b'4':
                _bool = self.Check()
                if _bool:
                    break
            else:
                break
        self.request.close()

class ThreadedServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class ForkedServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":
    HOST, PORT = '0.0.0.0', 10003
    print("HOST:POST " + HOST+":" + str(PORT))
    server = ForkedServer((HOST, PORT), Task)
    server.allow_reuse_address = True
    server.serve_forever()