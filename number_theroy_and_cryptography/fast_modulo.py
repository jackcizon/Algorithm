# Python3 program to compute
# exponential value
# using (2^k) -ary method.

# prime modulo value
N = 7

def fm(bas, exp):
	t = 1
	c = 0
	while(exp > 0):
		c += 1
		# for cases where exponent
		# is not an even value
		if (exp % 2 != 0): #if exp is odd, then excute >=2 times, first and last one in the loop, or others. if even, then the last one step must excute >= 1 times 
			t = (t * bas) % N #base is change, until exp == 0

		bas = (bas * bas) % N # m is large, 5 mod m == 5, 25 mod m = (5 mod m * 5 mod m) mod m == 25, ... 
		exp = int(exp / 2) #2^n n == 0 -> 1 list(exp) is geometric progression

	print(c)
	return t % N

# Driver Code
bas = 5
exp = 100

modulo = fm(bas,exp)
print(modulo)

# This code is contributed
# by mits
