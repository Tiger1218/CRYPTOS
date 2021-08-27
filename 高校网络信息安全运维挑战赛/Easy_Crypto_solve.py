from Crypto.Cipher import ARC4
rc4 = ARC4.new(b"hello world")
f = open("Easy_Crypto_enc.txt" , "rb")
flag = rc4.decrypt(f.read())
print(flag)