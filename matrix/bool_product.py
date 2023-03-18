def bool_product(A, B):
    C = [
            [0 for column in range(len(B[0])) ] for row in range(len(A))
        ]
    '''
        Bitwise operators:
            not: ~
            xor: ^
            and: &
            or : |
            left shift : <<
            right shift: >>
    '''
    for row in range(len(A)):
    
        for column in range(len(B[0])):
    
            for i in range(len(B)):
    
                C[row][column] |= (A[row][i] & B[i][column])
    
    print(C)


a = [
        [1, 0], 
        [0, 1], 
        [1, 0]
    ]

b = [
        [1, 1, 0],
        [0, 1, 1]
    ]



bool_product(a, b)