def sqrt(x):
    i = 0
    guess = x
    while i <5 and guess*guess != x:
        guess = (guess + x/guess)/2
        i += 1
    print(guess)
    return guess


def squareRoot(n, l) :

	x = n

	while (True) :
		root = 0.5 * (x + (n / x))

		if (abs(root - x) < l) :
			break

		x = root

	return root

if __name__ == "__main__" :

	n = 327
	l = 0.00001

	print(squareRoot(n, l))


'''
    newton method :
        f(Xn+1) - f(Xn) = f'(X) * (Xn+1 - Xn)  
        
        if f(Xn+1)=0  -->>  Xn+1 = Xn - (f(Xn) / f'(Xn))  ----  (1)
        
        specific case : halen to cal sqrt
        
                  sqrt(N) = Xn+1 = (Xn + N / Xn) / 2  -------   (2)

                  (1) == (2)   -->>   Xn - f(Xn) / f'(Xn) = (Xn + N / Xn) / 2   ==>>   f'(X) = -2*x  

                  f(x) = const(a) - x^2   -->> a = N
'''

sqrt(100)