from FLAG import flag
from Crypto.Cipher import AES

def pad(plain):
    padlen = 16 - len(plain) % 16
    return plain + bytes([padlen] * padlen)

XOR = lambda s1,s2 :bytes([x1^x2 for x1,x2 in zip(s1,s2)])

def my_cbc_encrypt(plain ,key, iv):
    plain = pad(plain)
    blocks = [plain[i*16:i*16+16] for i in range(len(plain)//16)]
    cipher = b''
    aes = AES.new(key , AES.MODE_ECB)
    for i in range(len(blocks)-1 , -1 , -1):
        iv = aes.encrypt(XOR(iv , blocks[i]))
        cipher = iv + cipher
    return cipher


if __name__ == "__main__":
    iv = b'welcometomssctf!'
    key = iv
    print(my_cbc_encrypt(flag ,key, iv))
    
#b'\xf7\xea\xfe\x00\xb9w\xa2f\xa2\xec\x1e*,\xe7|)O=\xf0~\xd4{\x06\x11hi\xcc<\xb2@{Jn$\xe3\xefZ8\xfaUE\xb6\xe0\x0eM\xc0\xcb\xc2\xa3 \x97\xb1\x8b:\xc8\x95\xdd`w\x0c%\x7f\xf6_\xbb\xd6\xac\x81F\x1a-\x82\x9f\x1a\x18\xd2\x0f\xa1\x8a5\xc9\xf7\xbe\xe2\xb0\xc0)\x03\x82\xf4\xee\xed4\x9c8/\xa3\x99D6vk\xf2\xfc\xf87\x1f\x83\xd3\xd77\xb6\xf9?\xe9\xd2\xbf;\xd6\x11\xba\xcbvS\x86\xc6\xaf\t\xce1\x17a\x1c\x89\x1e\xb8\xaa\x9f\xa0/\x08\x0f\xb3#'