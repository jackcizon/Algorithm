# Python3 program to check if N is Fermat pseudoprime
# to the base A or not


'''
pesudoprime:

    a^(p - 1) = k * m + 1
'''

from math import sqrt


def checkcomposite(n):
	
	# Check if there is any divisor of n less than sqrt(n)
	for i in range(2,int(sqrt(n))+1,1):
		if (n % i == 0):
			return 1
	return 0

# Effectively calculate (x^y) modulo mod
def power(x, y, mod):
	# Initialize result
	res = 1

	while (y):
		# If power is odd, then update the answer
		if (y & 1):
			res = (res * x) % mod

		# Square the number and reduce
		# the power to its half
		y = y >> 1
		x = (x * x) % mod

	# Return the result
	return res

# Function to check for Fermat Pseudoprime
def Check(n,a):
	# If it is composite and satisfy Fermat criterion
	if (a>1 and checkcomposite(n) and power(a, n - 1, n) == 1):
		return 1

	# Else return 0
	return 0

# Driver code
if __name__ == '__main__':
	N = 645
	a = 2
	print(Check(N, a))

