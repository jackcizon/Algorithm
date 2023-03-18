'''
A number is a perfect number if is equal to sum of its proper divisors,

that is, sum of its positive divisors excluding the number itself.
'''


def is_perfect(n):
    
    if n <= 1:
        return False

    sum = 1
    i = 2

    while i * i <= n:
        
        if n % i == 0:
            sum += i + n / i

        i += 1

    return True if sum == n else False


print(is_perfect(8))