import timeit


def is_prime(n):
    
    if n < 2:
        return False

    i = 2

    while i * i <= n:
        
        if n % i == 0:
            return False

        i += 1
    
    return True


def is_prime_optimize(n):
    
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


def main():

    begin1 = timeit.default_timer()

    is_prime(100011101)

    end1 = timeit.default_timer()

    print("excute time 1: ",float(end1 - begin1))



    begin2 = timeit.default_timer()

    is_prime_optimize(1000111101)

    end2 = timeit.default_timer()

    print('excute time 2: ', float(end2 - begin2))

    count = 0
    for i in range(100):
        if is_prime(i):
            count += 1

    print(count)

if __name__ == '__main__':
    main()




