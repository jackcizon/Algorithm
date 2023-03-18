a = [
        [9, 2], 
        [1, 5], 
        [11, 8]
    ]

def transpose(A):
    temp =  [
                [0 for _ in range(len(A))] for _ in range(len(A[0]))
            ]
    
    for i in range(len(A)):
    
        for j in range(len(A[0])):
            temp[j][i] = A[i][j]
    
    print(temp)


transpose(a)