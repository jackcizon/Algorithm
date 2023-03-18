# A Python program to check if a number is
# Carmichael or not.

'''
1. composite
2. gcd(b, n) = 1
3. b^(n-1) = k * n + 1
'''


# utility function to find gcd of two numbers
def gcd( a, b) :
	if (a < b) :
		return gcd(b, a)
	if (a % b == 0) :
		return b
	return gcd(b, a % b)

# utility function to find pow(x, y) under
# given modulo mod
def power(x, y, mod) :
	if (y == 0) :
		return 1
	temp = power(x, y // 2, mod) % mod
	temp = (temp * temp) % mod
	if (y % 2 == 1) :
		temp = (temp * x) % mod
	return temp


# This function receives an integer n and
# finds if it's a Carmichael number
def isCarmichaelNumber( n) :
	b = 2
	while b<n :
		
		# If "b" is relatively prime to n
		if (gcd(b, n) == 1) :

			# And pow(b, n-1)% n is not 1,
			# return false.
			if (power(b, n - 1, n) != 1):
				return 0
		b = b + 1
	return 1

# Driver function
print (isCarmichaelNumber(500))
print (isCarmichaelNumber(561))
print (isCarmichaelNumber(1105))

# This code is contributed by Nikita Tiwari.
