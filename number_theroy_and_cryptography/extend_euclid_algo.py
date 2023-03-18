'''
    we define function to understand EEA:

        e.g.: 2 = 6*x + 4*y

        we know 1 equation can get inifinte tuple for
        x an y,only 2 equations get unique x, y

        or let Z = F(f(x)f(y))
        this example: 
          z = 2 , f(x) = a*x, f(y) = b*y
          2 = 6x + 4y
          is plane of z = 2, which has inifity points
'''

'''
def extend_eculid(A, B):

    a, b = 0, 1

    x, y = 1, 0
    
    while A != 0:

        q, rem = B // A, B % A # get gcd
    
        m, n = a - x * q, b - y * q
    
        B, A = A, rem

        a, b = x, y

        x, y = m, n

    gcd = B

    return gcd, a, b


print(extend_eculid(6, 8))
'''

# Python program to demonstrate working of extended
# Euclidean Algorithm

# function for extended Euclidean Algorithm


def egcd(A, B):

	# Base Case
	if A == 0:
		return B, 0, 1

	gcd, x, y = egcd(B % A, A)

	q = B // A
	a = y - q * x
	b = x

	return gcd, a, b


print(egcd(3, 10))


'''
                                                                //==>> so egcd(6, 8) == 2, -1, 1 and return the result
recursion:                                                      ||
    1. when A = 6, B = 8, if not satify, return egcd(2, 6) == gcd, x, y
        ||                                                      /\
        || then pass gcd, 2, 6 to gcd, a, b.                    ||  ==>> so egcd(2, 6) == 2, 1, 0, claculate a = 0 - (8//6)*1 = -1, b = 1
        \/                                                      ||
    2. when A = 2, B = 6, if not satify, return egcd(0, 2) == gcd, x, y
        ||                                                      /\                      gcd  x  y
        || then pass gcd, 0, 2 to gcd, a, b.                    ||  ==>> so egcd(0, 2) == 2, 0, 1, calculete a = y - q * x = 1 - (6//2)*0 = 1, b = x = 0, and pass to caller(1)
        \/                                                      ||
    3. when A = 0, B = 2,if now satify, so gcd = 2, return 2, 0, 1 to its caller(2)
'''



def extended_euclid_gcd(a, b):
    """
    Returns a list `result` of size 3 where:
    Referring to the equation ax + by = gcd(a, b)
        result[0] is gcd(a, b)
        result[1] is x
        result[2] is y 
    """
    '''
    Si = Si-2 - Qi-1 * Si-1
    Ti = Ti-2 - Qi-1 * Ti-1

    S0 = 1, S1 = 0
    T0 = 0, T1 = 1
    '''
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r # In Python, // operator performs integer or floored division
        # This is a pythonic way to swap numbers
        # See the same part in C++ implementation below to know more
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

res = extended_euclid_gcd(24, 18)

'''
print 'GCD of 24 and 18 is %d. x = %d and y = %d in 24x + 18y = gcd(24, 18)' % (res[0], res[1], res[2])
# Output: GCD of 24 and 18 is 6. x = 1 and y = -1 in 24x + 18y = gcd(24, 18)
res = extended_euclid_gcd(54, 36)
print 'GCD of 54 and 36 is %d. x = %d and y = %d in 54x + 36y = gcd(54, 36)' % (res[0], res[1], res[2])
# Output: GCD of 54 and 36 is 18. x = 1 and y = -1 in 54x + 36y = gcd(54, 36)
res = extended_euclid_gcd(120, 428860)
print 'GCD of 120 and 428860 is %d. x = %d and y = %d in 120x + 428860y = gcd(120, 428860)' % (res[0], res[1], res[2])
# Output: GCD of 120 and 428860 is 20. x = 3574 and y = -1 in 120x + 428860y = gcd(120, 428860)
res = extended_euclid_gcd(95642, 1681)
print 'GCD of 95642 and 1681 is %d. x = %d and y = %d in 95642x + 1681y = gcd(95642, 1681)' % (res[0], res[1], res[2])
# Output: GCD of 95642 and 1681 is 1. x = 682 and y = -38803 in 95642x + 1681y = gcd(95642, 1681)
'''