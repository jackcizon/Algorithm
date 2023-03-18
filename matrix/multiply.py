#(m X k) * (k X n) -> (m X n)
#len(B[0]): column of B
#  len(A) :  row of A

def multiply(A, B):
    
    C = [
            [0 for i in range(len(B[0]))] for j in range(len(A))   
        ]
    
    for i in range(len(A)):

        for j in range(len(B[0])):

            for q in range(len(B)):
                C[i][j] = C[i][j] + A[i][q] * B[q][j]

    print(C)


a = [
        [9, 2], 
        [1, 5], 
        [11, 8]
    ]

b = [
        [2, 1, 7],
        [5, 4, 9]
    ]

multiply(a, b)
