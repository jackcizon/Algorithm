
'''
    a[i + 1] = ((a[i] * multipler) + increment) % modulo_number
'''

def linearCongruentialMethod(Xo, m, a, c,
							randomNums,
							noOfRandomNums):

	# Initialize the seed state
	randomNums[0] = Xo

	# Traverse to generate required
	# numbers of random numbers
	for i in range(1, noOfRandomNums):
		
		# Follow the linear congruential method
		randomNums[i] = ((randomNums[i - 1] * a) +
										c) % m

# Driver Code
if __name__ == '__main__':
	
	# Seed value
	Xo = 5
	
	# Modulus parameter
	m = 7
	
	# Multiplier term
	a = 3
	
	# Increment term
	c = 3

	# Number of Random numbers
	# to be generated
	noOfRandomNums = 10

	# To store random numbers
	randomNums = [0] * (noOfRandomNums)

	# Function Call
	linearCongruentialMethod(Xo, m, a, c,
							randomNums,
							noOfRandomNums)

	# Print the generated random numbers
	for i in randomNums:
		print(i, end = " ")
