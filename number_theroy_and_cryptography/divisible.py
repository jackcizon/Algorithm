'''
    c = a | b <=> c = b / a

    if n(int) | d(d > 0):
        exist k * d + r(0 <= r < d) = n
        k != 0 , k(int)
'''

#(int)(-3.2) = -3
#type(-33 / 11) is float
def division(n1, n2):

    if n1 > 0 and n2 > 0:
        
        if n1 > n2:
            return (int)(n1 / n2), n1 - (int)(n1 / n2) * n2
        
        else:
            return (int)(n2 / n1), n2 - (int)(n2 / n1) * n1
    
    elif n1 < 0 and n2 > 0:

            #return int(n1 / n2) - 1, 
            q = int(n1 / n2) - 1
            r = n1 - q * n2
            if r == 11:
                q += 1
                r = 0
            return q, r

    elif n2 < 0 and n1 > 0:
 
            q = int(n2 / n1) - 1
            r = n2 - q * n1
            
            if r == 11:
                q += 1
                r = 0
            return q, r


print(division(11, -3))
