'''
Given a prime number n, the task is to find its primitive root under modulo n. 

The primitive root of a prime number n is an integer r between[1, n-1] 

such that the values of r^x(mod n) where x is in the range[1, n-1] are different.

 Return -1 if n is a non-prime number.
'''


import sys

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


def is_primitive_root(r, n):
    
    if not is_prime(n) or r > n or r < 0:
        return False

    arr = [-1 for i in range(n - 1)]

    for i in range(1, n):
        arr[i - 1] = pow(r, i) % n

    for i in range(len(arr) - 1):
        
        for j in range(i + 1, len(arr), 1):
            
            if arr[i] == arr[j]:
                return False

    return True


print(is_primitive_root(4, 5))
'''
4^1 % 5 != 4^2 % 5 != 4^3 % 5 != 4^4 % 5
'''
