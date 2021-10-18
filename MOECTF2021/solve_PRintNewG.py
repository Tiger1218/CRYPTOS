# from sage.all import *
n = 164955381960104851576442781839629371483790790743830073857213053104860144345367
s1 = 67066424717605861916529090048670931008913194546199003522357504998012803616537
s2 = 14585402872351563180055857554749250191721167730349724393021149201170995608751
s3 = 68393939370424772490169906192546208899639826391163845848999554903218827210979
# var("seed a b")
# [d] = solve_mod([seed * a + b == s1 , s1 * a + b == s2 , s2 * a + b == s3], n, solution_dict = True)
# print(d[seed])
# In fact , Sagemath cannot solve this problem (
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

from Crypto.Util.number import *



def crack_unknown_increment(states, modulus, multiplier):
    increment = (states[1] - states[0]*multiplier) % modulus
    return modulus, multiplier, increment

def crack_unknown_multiplier(states, modulus):
    multiplier = (states[2] - states[1]) * inverse(states[1] - states[0], modulus) % modulus
    return crack_unknown_increment(states, modulus, multiplier)

_ , mu , inc = crack_unknown_multiplier([s1,s2,s3] , n)

print(long_to_bytes(( (s1 - inc) * inverse(mu , n) ) % n))