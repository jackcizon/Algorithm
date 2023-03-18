'''
    highest common factor :
        HCF(a, b) = 1

    attri:

    1. a, b can be composite

    2. 0 is not co-prime with any other number

    3. even numbers can never be co-prime

    4. If we add two co-prime numbers and multiply them, the resulting numbers are also co-prime.
    5. An odd number and an even number are also co-prime. However, if the numbers have 0 and 5 at the ones or unit places, they are not co-prime because they have an HCF = 5.
Prime numbers are co-prime numbers.

'''

import math

def co_prime(a, b):
    if math.gcd(a, b) == 1:
        return True
    else:
        return False
