'''
Cunningham Number is a number N 

of the form a^b + 1 or a^b - 1,

where a, b >= 2.
'''

import math

# Function to check if a number
# can be expressed as a^b.
def isPower(a):
	
	if (a == 1):
		return True
	
	i = 2
	while(i * i <= a):
		val = math.log(a) / math.log(i)
		if ((val - int(val)) < 0.00000001):
			return True
		i += 1
	return False
	
# Function to check if N is a
# Cunningham number
def isCunningham(n):
	return isPower(n - 1) or isPower(n + 1)
	
# Driver Code

# Given Number
n = 126

# Function Call
if (isCunningham(n)):
	print("Yes")
else:
	print("No")

