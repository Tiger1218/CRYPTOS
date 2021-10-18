from Crypto.Util.number import*
from Crypto.Cipher import AES
from secret import flag,theplain
from hashlib import sha256
import socketserver
import signal
import string
import random
import os

table = string.ascii_letters+string.digits

MENU = br'''[+] 1.Get BlackBird's Cipher:
[+] 2.Encrypt your Plaintext by BlackBird's Machine:
[+] 3.Exit:
[+] 4.Guess What BlackBird sent:
'''

BLANK = br'''
            .oooooo.     .oooooo.     .oooooo.     .oooooo.             oooooooooooo oooooooooooo oooooooooooo oooooooooo.  
           d8P'  `Y8b   d8P'  `Y8b   d8P'  `Y8b   d8P'  `Y8b            `888'     `8 `888'     `8 `888'     `8 `888'   `Y8b 
 .ooooo.  888      888 888      888 888      888 888      888  .ooooo.   888          888          888          888     888 
d88' `88b 888      888 888      888 888      888 888      888 d88' `88b  888oooo8     888oooo8     888oooo8     888oooo888' 
888   888 888      888 888      888 888      888 888      888 888   888  888    "     888    "     888    "     888    `88b 
888   888 `88b    d88' `88b    d88' `88b    d88' `88b    d88' 888   888  888          888          888          888    .88P 
`Y8bod8P'  `Y8bood8P'   `Y8bood8P'   `Y8bood8P'   `Y8bood8P'  `Y8bod8P' o888o        o888o        o888o        o888bood8P'  
'''

def pad(m):
    padlen = 16 - len(m) % 16
    return m + padlen * bytes([padlen])

def xor(msg1,msg2):
    assert len(msg1)==len(msg2)
    return long_to_bytes(bytes_to_long(msg1)^bytes_to_long(msg2))

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
        proof = (''.join([random.choice(table)for _ in range(20)])).encode()
        sha = sha256( proof ).hexdigest().encode()
        self.send(b"[+] sha256(XXXX+" + proof[4:] + b") == " + sha )
        XXXX = self.recv(prompt = b'[+] Plz Tell Me XXXX :')
        if len(XXXX) != 4 or sha256(XXXX + proof[4:]).hexdigest().encode() != sha:
            return False
        return True

    def Encrypt(self,plaintext):
        self.plain = plaintext
        aes = AES.new(self.key,AES.MODE_OFB,self.ivv)
        self.cipher = aes.encrypt(self.plain)
        return self.cipher

    def Opt1(self):
        return self.Encrypt(pad(theplain))

    def Opt2(self,plaintext):
        return self.Encrypt(pad(plaintext))

    def Opt4(self,guess):
        if guess == theplain:
            return flag
        else:
            return None

    def handle(self):
        signal.alarm(50)
        if not self.proof_of_work():
            return
        self.send(BLANK)
        self.send(b'\\\\\\\\~~~~~~=====================||||  Congratulations on Reaching the Final   ^v^ ||||=======================~~~~~~////')
        self.send(b'\\\\\\\\\\__________________________||||Today,let\'s guess what BlackBird sent to Noah.||||____________________________/////')
        self.ivv = os.urandom(16)
        self.key = os.urandom(16)
        while 1:
            self.send(MENU,newline = False)
            option = self.recv()
            if (option == b'1'):
                self.send(b"[~]BlackBird: I will give you the Encrypted Plain....\>_</...")
                self.send(b'                  Cipher is:' + self.Opt1())
            elif option == b'2':
                self.send(b"[~]BlackBird\'s Machine: .oO0Oo.kKk, input the plaintext,and I'll give you the Cipher....\>_</...")
                plaintext = self.recv()
                self.send(b'PlainText:' + plaintext + b'\nCipherText:' + self.Opt2(plaintext))
            elif option == b'4':
                self.send(b"[~]One day BlackBird sent theplain to Noah,then Noah gave him the flag.")
                self.send(b"[~]So,let\'s guess what BlackBird sent to Noah:")
                guess = self.recv()
                flag = self.Opt4(guess)
                if flag:
                    self.send(b"[~] w0W! c0ngr4tul4t1on5!\n...\^_^/...\nflag is " + flag + b'\n')
                break
            else:
                break
        self.send(b"\n[.]...the connection is closed............ =.= ............")
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