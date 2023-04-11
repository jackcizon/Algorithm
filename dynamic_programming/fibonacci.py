def fib(n):
    F = [0 for _ in range(n)]
    F[0] = F[1] = 1
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]

    return F[n - 1]


def main():
    print(fib(3))


if __name__ == '__main__':
    main()

