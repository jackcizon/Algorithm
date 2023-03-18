import math
import time 


def prime_factor(mersenne_prime):

    start = time.time()

    #factor = []

    while mersenne_prime % 2 == 0:
        #factor.append(2)
        yield 2
        mersenne_prime //= 2

    for i in range(3, int(math.sqrt(mersenne_prime) + 1), 2):
        while mersenne_prime % i == 0:
            #factor.append(i)
            yield i
            mersenne_prime //= i

    if mersenne_prime > 2:
        #factor.append(mersenne_prime)
        yield mersenne_prime 

    end = time.time()

    print("execute time : {}".format(end - start))

    #return factor


def main():
    mersenne_prime = pow(2, 100) - 1
    for i in prime_factor(mersenne_prime):
        print(i)
    #factor = prime_factor(mersenne_prime)
    #print(factor)


if __name__ == '__main__':
    main()




