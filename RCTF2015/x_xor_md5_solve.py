xors = n = ['69','35','41','01','1C','9E','75','78','5D','48','FB','F0','84','CD','66','79',
'55','30','49','4C','56','D2','73','70','12','45','A8','BA','85','C0','3E','53',
'73','1B','78','2A','4B','E9','77','26','5E','73','BF','AA','85','9C','15','6F',
'54','2C','73','1B','58','8A','66','48','5B','19','84','B0','80','CA','33','73',
'5C','52','0C','4C','10','9E','32','37','12','0C','FB','BA','CB','8F','6A','53',
'01','78','0C','4C','10','9E','32','37','12','0C','FB','BA','CB','8F','6A','53',
'01','78','0C','4C','10','9E','32','37','12','0C','FB','BA','CB','8F','6A','53',
'01','78','0C','4C','10','9E','32','37','12','0C','89','D5','A2','FC']

m = ['01','78','0C','4C','10','9E','32','37','12','0C','FB','BA','CB','8F','6A','53']
j = 0
s = ""
num = []
for i in range(0,len(n)):
	x = int(n[i],16)
	if j >= 16:
		j = 0 
	y = int(m[j],16)
	j += 1
	num.append(hex(x^y)[2:])
	s += chr(x^y)
print(num)
print(s)

num = ['68', '4d', '4d', '4d', '0c', '00', '47', '4f', '4f', '44', '00', '4a', '4f', '42', '0c', '2a', 
'54', '48', '45', '00', '46', '4c', '41', '47', '00', '49', '53', '00', '4e', '4f', '54', '00', 
'72', '63', '74', '66', '5b', '77', '45', '11', '4c', '7f', '44', '10', '4e', '13', '7f', '3c', 
'55', '54', '7f', '57', '48', '14', '54', '7f', '49', '15', '7f', '0a', '4b', '45', '59', '20', 
'5d', '2a', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 
'00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '72', '6f', '69', '73']

ss = ""
num2 = []
for i in range(0,len(num)):
	x = int(num[i],16)
	num2.append(hex(x^32)[2:])
	ss += chr(x^32)
print(num2)
print(ss)

#查看字符串，发现有个不对劲的地方，猜测key被两个*包括，即*key*，所以就是00^2a,所以不对劲的地方1c^2a得到36，所以正确的列表如下

num2 = ['48', '6d', '6d', '6d', '2c', '20', '67', '6f', '6f', '64', '20', '6a', '6f', '62', '2c', '0a', 
'74', '68', '65', '20', '66', '6c', '61', '67', '20', '69', '73', '20', '6e', '6f', '74', '20', 
'52', '43', '54', '46', '7b', '57', '65', '31', '6c', '5f', '64', '30', '6e', '33', '5f', '36', 
'75', '74', '5f', '77', '68', '34', '74', '5f', '69', '35', '5f', '2a', '6b', '65', '79', '2a', 
'7d', '0a', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', 
'20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', 
'20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '20', 
'20', '20', '20', '20', '20', '20', '20', '20', '20', '20', '52', '4f', '49', '53']

xx = ""
for i in range(0,len(num2)):
	xx += chr(int(num2[i],16))
print(xx) 

zz = []
for i in range(0,len(m)):
	x = int(m[i],16)
	zz.append(hex(x^32)[2:])
print(zz)