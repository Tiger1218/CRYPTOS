from flag import flag
dic = { 'a': 'd','b': 'f','c': 's','d': 'z','e': 'b','f': 'q','g': 'a','h': 'r','i': 't','j': 'w','k': 'y','l': 'x','m': 'v','n': 'p','o': 'm','p': 'n','q': 'l','r': 'u','s': 'o','t': 'h','u': 'j','v': 'k','w': 'i','x': 'g','y': 'e','z': 'c'}

def main():
    c = ''
    for _ in flag:
        c = c+dic[_]
    print(c)

if __name__ == "__main__":
    main()
'''
output:
dqqtpbtodxombdoe
'''