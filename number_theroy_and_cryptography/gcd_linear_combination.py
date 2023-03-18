'''
Let gcd(a,b)=d
 We are given that n=xd
 for some x∈Z

Now expand d
 using Bezout's identity. We know d=sa+tb
 for some s,t∈Z
. Hence:

n=xd=x(sa+tb)=xsa+xtb
And we recognize this as a linear combination
 of a and b
'''

import math

def gcd_linear_combination(a, b, c):
    
    return (c % math.gcd(a, b) == 0)


print(gcd_linear_combination(6, 8, 100))