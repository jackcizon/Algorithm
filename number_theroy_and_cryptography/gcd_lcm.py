def gcd(a, b):
    
    if b == 0:
        return a
    
    else:
        return gcd(b, a % b)

print(gcd(9888, 6060))


def lcm(a, b):
        
    return a * b / gcd(a, b)


print(lcm(100012, 4568))