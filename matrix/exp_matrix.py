import timeit

def multiply(A, B):
    
    C = [
            [0 for _ in range(len(B[0]))] for _ in range(len(A))   
        ]
    
    for i in range(len(A)):

        for j in range(len(B[0])):

            for q in range(len(B)):
                C[i][j] = C[i][j] + A[i][q] * B[q][j]

    return C


'''
    iteration 
'''
def exp(A, n):
    
    if len(A) != len(A[0]):
        raise Exception("can't operation to except NxN matrix")

    temp = [0 for _ in range(len(A[0])) for _ in range(len(A))]

    temp = A

    for _ in range(1, n):

        temp = multiply(A, temp)

    return temp


'''
    fast recusion
'''
def exp_optimize(A, n):
    
    if len(A) != len(A[0]):
        raise Exception("can't operation to except NxN matrix")
    '''
    temp = [0 for _ in range(len(A[0])) for _ in range(len(A))]

    if n == 0:
        return temp 
    '''
    if n == 1:
        return A

    if n % 2 == 0:
        return multiply(exp_optimize(A, n // 2), exp_optimize(A, n // 2))

    else:
        
        return multiply(A, exp_optimize(A, n - 1))

a = [
        [1, 0],
        [1, 1]
    ]


def main():

    begin1 = timeit.default_timer()
    print(exp(a, int(1e5)))
    end1 = timeit.default_timer()
    print("normal execute time : {}".format(float(end1 - begin1)))


    begin2 = timeit.default_timer()
    print(exp_optimize(a, int(1e5)))
    end2 = timeit.default_timer()
    print("optimize execute time : {}".format(float(end2 - begin2)))



if __name__ == '__main__':
    main()
