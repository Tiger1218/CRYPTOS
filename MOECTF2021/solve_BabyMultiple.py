cipher = 'g3AfJPOfHPOJFfJuf_AYux1JFx39'
table = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
transtable = ''
for i in range(len(table)):
    transtable += table[(58 * i) % 63]
print(transtable)
dicts = {transtable[i] : table[i] for i in range(63)}
for i in cipher:
    print(dicts[i] , end="")