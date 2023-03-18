def sum_to_product(a, b):
	
	i = 0 
	s = [0 for i in range(32)]
	prod = 0
	rem = 0

	while(a != 0 or b != 0):
		s[i] = (a % 10 + b % 10 + rem) % 2
		rem = (int)((a % 10 + b % 10 + rem) / 2)
		a = (int)(a / 10)
		b = (int)(b / 10)
		i += 1

	if rem != 0:
		s[i] = rem
	'''
	above is sum is 11001
    and we add them get product
	'''

	while i >= 0:
		prod = prod * 10 + s[i]
		i -= 1
	'''
	we input as binary, but decimal, so we need  by 10 each bit,then add,
	 though we konw result is actual decimal, but it display as bianry
	'''

	return prod

def product(a, b):

	multiply = 0
	digit = 0
	factor = 1

	while b != 0:
		digit = b % 10

		if digit == 1:
			'''
			whether b2[i] is 0 or 1, b1 must by 10 to shift bit
			'''

			a = a * factor
			multiply = sum_to_product(a, multiply)

		else:
			a = a * factor

		b = (int)(b / 10)
		factor = 10

	print("product : {}".format(multiply))


product(101, 101)