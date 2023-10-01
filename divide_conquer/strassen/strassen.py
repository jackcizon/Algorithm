import numpy as np
import time

def brute_force(A, B):
    n, m, p = A.shape[0], A.shape[1], B.shape[1]
    C = np.array([[0] * p for _ in range(n)])
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C

def split(matrix):
    n = len(matrix)
    m = n // 2  # Ensure even split
    return matrix[:m, :m], matrix[:m, m:], matrix[m:, :m], matrix[m:, m:]

def strassen2(A, B):
    if len(A) <= 2:
        return brute_force(A, B)
    a, b, c, d = split(A)
    e, f, g, h = split(B)
    ae = strassen2(a, e)
    bg = strassen2(b, g)
    af = strassen2(a, f)
    bh = strassen2(b, h)
    ce = strassen2(c, e)
    dg = strassen2(d, g)
    cf = strassen2(c, f)
    dh = strassen2(d, h)
    C11 = ae + bg
    C12 = af + bh
    C21 = ce + dg
    C22 = cf + dh
    C = np.vstack(
        (np.hstack((C11, C12)),
         np.hstack((C21, C22))
         ))
    return C

def strassen(A, B):
    if len(A) <= 2:
        return brute_force(A, B)
    a, b, c, d = split(A)
    e, f, g, h = split(B)
    p1 = strassen(a + d, e + h)
    p2 = strassen(d, g - e)
    p3 = strassen(a + b, h)
    p4 = strassen(b - d, g + h)
    p5 = strassen(a, f - h)
    p6 = strassen(c - d, e + h)
    p7 = strassen(a - c, e + f)
    C11 = p1 + p4 - p5 + p7
    C12 = p3 + p5
    C21 = p2 + p4
    C22 = p1 - p2 + p3 + p6
    C = np.vstack(
        (np.hstack((C11, C12)),
         np.hstack((C21, C22))
         ))
    return C


n = 512
A = np.random.randn(n, n)
B = np.random.randn(n, n)
start = time.time()
C = strassen(A, B)
end = time.time()
execute_time = end - start
print("use strassen-algo takes {}s.".format(execute_time), end="\n")
start = time.time()
C = brute_force(A, B)
end = time.time()
execute_time = end - start
print("use BF-algo takes {}s.".format(execute_time), end="\n")

