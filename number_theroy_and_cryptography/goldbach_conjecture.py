'''
Every even integer greater than 2 can be expressed as the sum of two primes.
'''

'''
Find the prime numbers using Sieve of Sundaram

Check if the entered number is an even number greater than 2 or not, if no return.

If yes, then one by one subtract a prime from N and then check 

if the difference is also a prime. If yes, then express it as a sum.
'''


import math
MAX = 10000

# Array to store all prime less
# than and equal to 10^6
primes = []

# Utility function for Sieve of Sundaram
def sieveSundaram():
	
	# In general Sieve of Sundaram, produces
	# primes smaller than (2*x + 2) for a
	# number given number x. Since we want
	# primes smaller than MAX, we reduce
	# MAX to half. This array is used to
	# separate numbers of the form i + j + 2*i*j
	# from others where 1 <= i <= j
	marked = [False] * (int(MAX / 2) + 100)

	# Main logic of Sundaram. Mark all
	# numbers which do not generate prime
	# number by doing 2*i+1
	for i in range(1, int((math.sqrt(MAX) - 1) / 2) + 1):
		for j in range((i * (i + 1)) << 1,
						int(MAX / 2) + 1, 2 * i + 1):
			marked[j] = True

	# Since 2 is a prime number
	primes.append(2)

	# Print other primes. Remaining primes
	# are of the form 2*i + 1 such that
	# marked[i] is false.
	for i in range(1, int(MAX / 2) + 1):
		if (marked[i] == False):
			primes.append(2 * i + 1)

# Function to perform Goldbach's conjecture
def findPrimes(n):
	
	# Return if number is not even
	# or less than 3
	if (n <= 2 or n % 2 != 0):
		print("Invalid Input")
		return

	# Check only upto half of number
	i = 0
	while (primes[i] <= n // 2):
		
		# find difference by subtracting
		# current prime from n
		diff = n - primes[i]

		# Search if the difference is also
		# a prime number
		if diff in primes:
			
			# Express as a sum of primes
			print(primes[i], "+", diff, "=", n)
			return
		i += 1



# Finding all prime numbers before limit
sieveSundaram()

# Express number as a sum of two primes
findPrimes(4)
findPrimes(38)
findPrimes(100)