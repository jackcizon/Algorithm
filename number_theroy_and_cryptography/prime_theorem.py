'''
when x is growing infinity, numbers of prime 

that less than x equal to pi(x) / (X / lnX)

so probility of prime in range[0, n]  is (N / lnN) / N = (1 / lnN)  

pi(x) is function about numbers of prime less than x:
    pi(10^3) = 168
    pi(10^6) = 78498
    pi(10^10) = 455 052 512 
'''

import math

def e():
    exp = 0
    
    for i in range(32):
        exp += 1 / math.factorial(i)
        
    return exp


def is_prime(n):
    
    if n <= 1:
        return False

    if n <= 3:
        return True

    if n %2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False

        i += 6

    return True

def prime_theorem(x):
    lnx = math.log(x, e())
    return x / lnx
    

def main():

    num = (int)(math.pow(10, 6))

    n = (int)(prime_theorem(num))

    count = 0
    for i in range(num):
        if is_prime(i):
            count += 1

    if count - 10 < n or count + 10 > n:
        print("actual prime counts: {}, approximately:{}, divides {}".format(count, n, count / n))

if __name__ == '__main__':
    main()
