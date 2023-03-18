'''
A Twin prime are those numbers 

which are prime and having a difference of two ( 2 )

between the two prime numbers.

In other words, a twin prime is a prime that has a prime gap of two. 
'''


import math

def isPrime( n ):
	
	if n <= 1:
		return False
	if n <= 3:
		return True
	
	if n%2 == 0 or n%3 == 0:
		return False
	
	for i in range(5, int(math.sqrt(n)+1), 6):
		if n%i == 0 or n%(i + 2) == 0:
			return False
	
	return True


def twinPrime(n1 , n2):
	return (isPrime(n1) and isPrime(n2) and
					abs(n1 - n2) == 2)


n1 = 137
n2 = 139

if twinPrime(n1, n2):
	print("Twin Prime")
else:
	print("Not Twin Prime")
