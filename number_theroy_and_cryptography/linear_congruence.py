
def ExtendedEuclidAlgo(a, b):
	
	# Base Case
	if a == 0 :
		return b, 0, 1
		
	gcd, x1, y1 = ExtendedEuclidAlgo(b % a, a)
	
	# Update x and y using results of recursive
	# call
	x = y1 - (b // a) * x1
	y = x1
	
	return gcd, x, y
	
# Function to give the distinct
# solutions of ax = b (mod n)
def linearCongruence(A, B, N):
	
	A = A % N
	B = B % N
	u = 0
	v = 0
	
	# Function Call to find
	# the value of d and u
	d, u, v = ExtendedEuclidAlgo(A, N)
	
	# No solution exists
	if (B % d != 0):
		print(-1)
		return
	
	# Else, initialize the value of x0
	x0 = (u * (B // d)) % N
	if (x0 < 0):
		x0 += N
	
	# Pr all the answers
	for i in range(d):
		print((x0 + i * (N // d)) % N, end = " ")

# Driver Code

# Input
A = 15
B = 9
N = 18

# Function Call
linearCongruence(A, B, N)

# This code is contributed by SHUBHAMSINGH10
