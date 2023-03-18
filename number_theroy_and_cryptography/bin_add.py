from pprint import pprint as pp

def bin_add(a, b):
    
    s = [0 for i in range(32)]
    i = 0
    rem = 0

    while a != 0 or b != 0:
        s[i] = (a % 10 + b %10 + rem) % 2
        rem = (int)((a % 10 + b % 10 + rem) / 2)
        a = (int)(a / 10)
        b = (int)(b / 10)
        i += 1

        #if carry 1 bit
        if rem != 0:
            s[i] = rem

    for k in range(len(s) - 1, -1, -1):
        print(s[k],end="")


bin_add(10000, 11111)