'''
a function return values all primes
'''

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


#for int less than 41, return all primes
def generate_prime(n):
    fn = n * n - n + 41
    return fn


def main():
    sum = 41
    count = 0

    for i in range(sum):
        
        if is_prime(generate_prime(i)):
            count += 1

    if sum == count:
        print("generate function return all primes")


if __name__ == '__main__':
    main()