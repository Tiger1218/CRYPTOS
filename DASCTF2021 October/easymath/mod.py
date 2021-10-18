#要定义这个运算，需要三个整数。a的模逆元素（对n取模）为b，意味着a*b mod m=1，则称a关于m的模逆为b
def     gcd(a,b):
        while a!=0:
            a,b = b%a,a
        return b
#定义一个函数，参数分别为a,n，返回值为b
def     findModReverse(a,m):#这个扩展欧几里得算法求模逆

        if gcd(a,m)!=1:
            return None
        u1,u2,u3 = 1,0,a
        v1,v2,v3 = 0,1,m
        while v3!=0:
            q = u3//v3
            v1,v2,v3,u1,u2,u3 = (u1-q*v1),(u2-q*v2),(u3-q*v3),v1,v2,v3
        return u1%m

print(findModReverse(2**10000,10**175))