from Crypto.Util.number import long_to_bytes, bytes_to_long
from gmpy2 import mpz, to_binary
import random

ALPHABET = bytearray(b"0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ#")


def base_n_encode(bytes_in, base):
    return mpz(bytes_to_long(bytes_in)).digits(base).encode()

hello = b"hello,world"
for i in range(2,37):
    print(base_n_encode(hello , i))


# def base_n_decode(bytes_in, base):
#     bytes_out = to_binary(mpz(bytes_in, base=base))[:1:-1]
#     return bytes_out

# def encrypt(bytes_in, round):
#     out = bytes_in
#     for i in range(round):
#         while 1:
#             w1 = random.randint(2,len(ALPHABET))
#             out = base_n_encode(out, w1)
#             break
#     return out


# def decrypt(bytes_in, key):
#     out = bytes_in
#     for i in key:
#         out = base_n_decode(out, ALPHABET.index(i))
#     return out


# flag_enc = encrypt(flag, 12)
# with open('flag_enc','w') as f:
#     f.write(flag_enc.decode())
