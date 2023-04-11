def longest_common_substring(s1, s2):
    
    m = len(s1)
    n = len(s2)

    #table[n+1][m+1]
    table = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    result = 0
    
    end_point = 0 
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                table[i][j] = table[i - 1][j - 1] + 1
                if table[i][j] > result:
                    result = table[i][j]
                    end_point = i
            else:
                table[i][j] = 0

    return s1[end_point - result: end_point]


def main():
    print(longest_common_substring('google', 'googlgoogo'))


if __name__ == '__main__':
    main()

'''
    e.g.         index:
             0 1 2 3 4 5 6 7 8
        0      j k a b c d m n
        1 j    1
index:  2 m                1
        3 a        1(result=3)
        4 b          2
        5 c            3(end_point=5) 
        
        so the s1[2:3]
'''