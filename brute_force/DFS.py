'''
    DFS is similar to BF.

    DFS can be implemented by using recursion.

    In this case, much like a binary decision tree.
'''

'''
                    i = 0
                    sum = 0
                    /    \.
                   /      \+1
               i = 1     i = 1
               sum=0     sum = 1
                /  \ +2       \.
               /    \          \.
            i = 2   i = 2 .........
            sum=0   sum=2 .........
        ............................
'''

'''
    this approach is 1 + 2 + 4 + ... + 2**count = O(2**(count+1))
'''

def DFS(arr, index, sum, key, count):
    
    #if iter_over, check sum == key
    if index == count:
        return sum == key 
    
    #do not add arr[i], path1
    if DFS(arr, index + 1, sum, key, count):
        return True
    
    #add arr[i], path2
    if DFS(arr, index + 1, sum + arr[index], key, count):
        return True

    return False 


def main():
    print(DFS([1, 2, 4, 7, 20], 0, 0, 13, 5))


if __name__ == '__main__':
    main()
