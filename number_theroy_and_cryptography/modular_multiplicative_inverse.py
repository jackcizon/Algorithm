'''
Given two integers A and M, find the modular multiplicative inverse of A under modulo M.

The modular multiplicative inverse is an integer X such that:

A * X = 1 + k * M
'''

'''
we print the inverse number if we find it
'''

def mod_inverse(A, M):
    for X in range(1, M):
        if ((A % M) * (X % M)) % M == 1:
            return X
    
    return -1


def modInverse(A, M):

	g = gcd(A, M)

	if (g != 1):
		print("Inverse doesn't exist")

	else:

		# If A and M are relatively prime,
		# then modulo inverse is A^(M-2) mod M
		print("Modular multiplicative inverse is ",
			power(A, M - 2, M))

# To compute x^y under modulo M


def power(x, y, M):

	if (y == 0):
		return 1

	p = power(x, y // 2, M) % M
	p = (p * p) % M

	if(y % 2 == 0):
		return p
	else:
		return ((x * p) % M)


def gcd(a, b):
	if (a == 0):
		return b

	return gcd(b % a, a)


def main():

    print(mod_inverse(3, 11))
    modInverse(3, 11)


if __name__ == '__main__':
    main()