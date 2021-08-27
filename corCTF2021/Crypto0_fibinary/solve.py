ciphertext = open("flag.enc" , "rb").read()
# print(ciphertext.split(b' '))
ciphertext = ciphertext.split(b' ')
fib = [1, 1]
for i in range(2, 11):
	fib.append(fib[i - 1] + fib[i - 2])

def c2f(c):
	n = ord(c)
	b = ''
	for i in range(10, -1, -1):
		if n >= fib[i]:
			n -= fib[i]
			b += '1'
		else:
			b += '0'
	return b

for i in ciphertext:
    for j in range(256):
        # print(c2f(chr(j)))
        # print(i , int(c2f(chr(j)) , 2))
        if c2f(chr(j)).encode() == i:
            
            print(chr(j) , end="")