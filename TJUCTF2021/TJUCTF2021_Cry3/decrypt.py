import hashlib

from Crypto.Cipher import AES

# from encrypt import calcRedundantBits, detectError, extractRedundantBits

NUM_REDUNDANT_BITS = 7


def pos_redundant_bits(data, r):
    # Place redundancy bits to the positions of the power of 2
    j = 0
    k = 1
    m = len(data)
    res = ''

    # Insert '0' to the positions of the power of 2
    for i in range(1, m + r + 1):
        if (i == 2 ** j):
            res = res + '0'
            j += 1
        else:
            res = res + data[-1 * k]
            k += 1

    return res[::-1]


def calc_parity_bits(arr, r):
    n = len(arr)

    # Searching for r parity bit
    for i in range(r):
        val = 0
        for j in range(1, n + 1):

            # If position has 1 in ith significant
            # position then Bitwise OR the array value
            # to find parity bit value.
            if (j & (2 ** i) == (2 ** i)):
                val = val ^ int(arr[-1 * j])
                # -1 * j is given since array is reversed

        # String Concatenation
        # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
        arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
    return arr


def calc_final_parity(arr):
    # Add a parity bit to the last bit of 128b string
    return "0" if arr.count("1") % 2 == 0 else "1"

def make_random_err(str):
    while 1:
        err_w = random.randint(0,len(str)-1)
        if bin(err_w)[2:].count('1') > 1:
            if str[err_w] == '1':
                return str[:err_w]+'0'+str[err_w+1:]
            else:
                return str[:err_w]+'1'+str[err_w+1:]

def hamming_encode_block(block):
    bin_block = ''.join([bin(bt)[2:].zfill(8) for bt in block])
    arr = pos_redundant_bits(bin_block, NUM_REDUNDANT_BITS)
    arr = calc_parity_bits(arr, NUM_REDUNDANT_BITS)
    arr += calc_final_parity(arr)
    arr = arr[::-1]
    arr = make_random_err(arr)
    return arr[::-1]

pub_msg = open("flag_enc.png", "rb") .read( )
rx_key_128 = hashlib.md5 ("tothemoon".encode()).digest()
rx_iv = pub_msg[:16]
rx_ctxt = pub_msg [16: ]

decryptor = AES.new( rx_key_128,AES.MODE_CBC,IV=rx_iv)
plain = decryptor.decrypt(rx_ctxt)

raw_blocks = [ ]
blocks = []
mistaken_blocks = []
parity_blocks = []
i=0
while len(plain):
	current_block = plain [ : 16]
	plain = plain [16: ]
	arr = ' '.join([bin(bt)[2:].zfill(8) for bt in current_block])
	parity_bit = arr[-1]
	arr = arr[:1]
	r = calcRedundantBits(15 * 8)
	raw_blocks.append(arr)
	parity_blocks.append(parity_bit)
	extr = extractRedundantBits(arr, r)
	bite_block = bytes(int(extr[i: i + 8], 2) for i in range(0, len(extr), 8))
	blocks.append(extr)

	if detectError(arr,r) != 0 and parity_bit == calc_final_parity(arr):
		mistaken_blocks.append(i)

	i += 1


for i in range(len(blocks) - 1,0,-1):
	correction = 127 - detectError( raw_blocks[i], r)

	if correction !=127:
		# when error in block and match parity bit
		if calc_final_parity( raw_blocks [i]) == parity_blocks[i]:
			print( f"Double mismatch on i={i}")

	arr = raw_blocks[i] [ :correction] + str(1 - int(raw_blocks[i][correction] )) + raw_blocks[i][correction]
	raw_blocks [i] = arr
	blocks [i] = extractRedundantBits(arr, 7)

	print(bytes(int(blocks[i][j: j +8], 2) for j in range(0, len(blocks[i]), 8)))

	padding = (i - 1) * 16
	encrypted_block = rx_ctxt [padding : padding +16]
	fb = ' '.join([bin(bt)[2:].zfill(8) for bt in encrypted_block])
	fb = fb[:correction] + str(1 - int(fb[correction] )) + fb[correction + 1:]
	fb = bytes(int(fb[i: i + 8], 2) for i in range(0, len(fb), 8))
	raw_text = decryptor.decrypt(rx_ctxt[ :padding] + fb + rx_ctxt [padding + 16:])
	raw_block = raw_text [padding:padding + 16]
	arr = ' '.join( [bin(bt)[2:].zfill(8) for bt in raw_block])
	new_parity_bit = arr[-1]
	arr = arr[:-1]

	raw_blocks [i - 1] = arr
	blocks [i - 1] = extractRedundantBits(arr,7)
	parity_blocks [i - 1] = new_parity_bit

txt = ' '.join(blocks)
plaintext = bytes(int(txt[i: i + 8], 2) for i in range(0, len(txt), 8))
plaintext = plaintext.rstrip(b'\x00')
with open("flag_decrypted.jpg", "wb") as w:
	w.write(plaintext)