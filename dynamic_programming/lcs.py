def lcs(s1, s2):
    c = [[0 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

    max_val = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            #first check diagonal
            if s1[i] == s2[j]:
                c[i+1][j+1] = c[i][j] + 1
            else:
                #check up and left
                c[i+1][j+1] = max(c[i][j+1], c[i+1][j])
            
            max_val = max(max_val, c[i+1][j+1])

    # backtrack to get the LCS string
    i, j = len(s1), len(s2)
    lcs_string = ''
    while i > 0 and j > 0:
        #we chose diagonal first if both up and left are equal to diagonal
        if s1[i-1] == s2[j-1]:
            lcs_string = s1[i-1] + lcs_string
            i -= 1
            j -= 1
        #up case
        elif c[i-1][j] > c[i][j-1]:
            i -= 1
        #left case
        else:
            j -= 1

    return lcs_string


def main():
    str = lcs('hello', 'hlo')
    print("the lcs is '{}'".format(str), end='\n')
    print("the str length is {}".format(len(str)))


if __name__ == '__main__':
    main()


'''
    e.g.:       s1:
        a   b   c   d   a   f
      ________________________
    0|  0   0   0   0   0   0   
s2:  |\\
a   0|  1   1   1   1   1   1     
     | /|\ 
c   0|  1   1   1   2   2   2   
     |   \\
b   0|  1   2   2   2   2   2  
     |       \\
c   0|  1   2   3===3===3   3
     |                   \\
f   0|  1   2   3   3   3   4

1. 'a'  match 'abcdaf'
2. 'ac' match 'abcdaf'
    .........
    .........
final:
    s1 match s2

this is path, and we backtrack follow by this way,
first choose diagonal, and then up and left
'''