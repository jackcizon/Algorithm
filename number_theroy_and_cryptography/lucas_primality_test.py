def lucas_lehmer(p):
        M = 2**p - 1
        s = 4
        for _ in range(p-2):
            s = (s*s - 2) % M
        return s == 0

print(lucas_lehmer(100))




# Python3 program for Lucas Primality Test
import random
import math

# Function to generate prime factors of n
def primeFactors(n, factors):
	
	# If 2 is a factor
	if (n % 2 == 0):
		factors.append(2)
		
	while (n % 2 == 0):
		n = n // 2
		
	# If prime > 2 is factor
	for i in range(3, int(math.sqrt(n)) + 1, 2):
		if (n % i == 0):
			factors.append(i)
			
		while (n % i == 0):
			n = n // i
			
	if (n > 2):
		factors.append(n)
		
	return factors
	
# This function produces power modulo
# some number. It can be optimized to
# using
def power(n, r, q):
	
	total = n
	
	for i in range(1, r):
		total = (total * n) % q
		
	return total

def lucasTest(n):

	# Base cases
	if (n == 1):
		return "neither prime nor composite"
	if (n == 2):
		return "prime"
	if (n % 2 == 0):
		return "composite1"
		
	# Generating and storing factors
	# of n-1
	factors = []
	
	factors = primeFactors(n - 1, factors)

	# Array for random generator. This array
	# is to ensure one number is generated
	# only once
	rand = [i + 2 for i in range(n - 3)]
		
	# Shuffle random array to produce randomness
	random.shuffle(rand)

	# Now one by one perform Lucas Primality
	# Test on random numbers generated.
	for i in range(n - 2):
		a = rand[i]
		
		if (power(a, n - 1, n) != 1):
			return "composite"

		# This is to check if every factor
		# of n-1 satisfy the condition
		flag = True
		
		for k in range(len(factors)):
			
			# If a^((n-1)/q) equal 1
			if (power(a, (n - 1) // factors[k], n) == 1):
				flag = False
				break

		# If all condition satisfy
		if (flag):
			return "prime"
	
	return "probably composite"
	
# Driver code
if __name__=="__main__":
	
	print(str(7) + " is " + lucasTest(7))
	print(str(9) + " is " + lucasTest(9))
	print(str(37) + " is " + lucasTest(37))

# This code is contributed by rutvik_56
