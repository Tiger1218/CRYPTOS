import base36
cipher0 = "7r7m11ftidw8a26ixbswjs7ldg5cni6vfswa8j567v5c2lv3cx28gkb9cfa2lk9h67o2techbzy07oiafnnshprkpaygt8qktf9"
cipher0 = int(cipher0 , 36)
cipher1 = "lw6o5k6qcfq1hgb2t2bstpmkwdslpczslqbietypqlj9oyysq93k28mseks77rjd7sbsnb6v5pl2wvk1t5ksrir2zlnwx9dwvlxvi4b02ukua02o9i48p"
cipher1 = int(cipher1 , 36)
table = "0123456789abcdefghijklmnopqrstuvwxyz"
table_rev = {'0' : 0 , }
# pow(e , r , p) == cipher0
e = 2333
p = 25837803107239222173952070863792093460107066132554083629904658720362290337547984488864287283444004000702302024445859946181490789947549247970591904040287281
h = 3157949570880104750798870795076886225888442155001709003841060612772039388989395218484005993511083988039042347782289369175775773651613878334013870511350162
# r = -1 遍历r
# for i in range(10000000):
#     if pow(e , i , p) == cipher0:
#         r = i
#         break

# print(r)
r = 4796904
rText = str(r)
rlen = len(rText)
b = cipher1 // pow(h , r , p)
text = base36.dumps(b)
for i in range(len(text)):
    j = i % rlen
    for xnumber in range(len(table)):
        if table[xnumber] == text[i]:
            for rnumber in range(len(table)):
                if table[rnumber] == rText[j]:
                    fnumber = (xnumber - rnumber) % 36
                    print(table[fnumber] , end="")