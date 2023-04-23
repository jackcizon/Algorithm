'''
    a matrix n * m

    4 cases:
        1. n is odd, m is odd

        2. n is even, m is even

        3. n is odd, m is even

        4. n is even, m is odd

'''

from pprint import pprint as pp

#for case 1, 2
def rotate(matrix):
    n = len(matrix)
    #a n*n matrix has int(n/2) layer, strart from 0(outside) to n/2 inside.
    for i in range(0, n//2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp



def main():
    matrix = [
        [1, 2, 3, 4],
        [4, 5, 6, 6],
        [7, 8, 9, 10],
        [3, 6, 4, 1]
    ]

    rotate(matrix)

    pp(matrix)


if __name__ == '__main__':
    main()