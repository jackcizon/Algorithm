'''
Given a number n, 

print all primes <= n.
'''
'''
1) In general Sieve of Sundaram, produces primes smaller than 
   (2*x + 2) for given number x. Since we want primes 
   smaller than n, we reduce n-1 to half. We call it nNew.
       nNew = (n-1)/2;
   For example, if n = 102, then nNew = 50.
                if n = 103, then nNew = 51

2) Create an array marked[n] that is going 
   to be used to separate numbers of the form i+j+2ij from 
   others where  1 <= i <= j

3) Initialize all entries of marked[] as false.

4) // Mark all numbers of the form i + j + 2ij as true
   // where 1 <= i <= j
   Loop for i=1 to nNew
        a) j = i; 
        b) Loop While (i + j + 2*i*j)  2, then print 2 as first prime.

6) Remaining primes are of the form 2i + 1 where i is
   index of NOT marked numbers. So print 2i + 1 for all i
   such that marked[i] is false. 

'''

# Prints all prime numbers smaller
def SieveOfSundaram(n):
	
	# In general Sieve of Sundaram,
	# produces primes smaller
	# than (2*x + 2) for a number
	# given number x. Since we want
	# primes smaller than n, we
	# reduce n to half
	nNew = int((n - 1) / 2)

	# This array is used to separate
	# numbers of the form i+j+2ij
	# from others where 1 <= i <= j
	# Initialize all elements as not marked
	marked = [0] * (nNew + 1)

	# Main logic of Sundaram. Mark all
	# numbers of the form i + j + 2ij
	# as true where 1 <= i <= j
	for i in range(1, nNew + 1):
		j = i
		while((i + j + 2 * i * j) <= nNew):
			marked[i + j + 2 * i * j] = 1
			j += 1

	# Since 2 is a prime number
	if (n > 2):
		print(2, end = " ")

	# Print other primes. Remaining
	# primes are of the form 2*i + 1
	# such that marked[i] is false.
	for i in range(1, nNew + 1):
		if (marked[i] == 0):
			print((2 * i + 1), end = " ")

# Driver Code
n = 20
SieveOfSundaram(n)