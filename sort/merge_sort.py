def merge(arr, left, mid , right):
    '''
    divide array in two parts
    '''
    size1 = mid - left + 1
    size2 = right - mid

    '''
    temp array:
        build two temp array save result,
        then merge them   
    '''
    L = [0] * size1
    R = [0] * size2

    for i in range(size1):
        L[i] = arr[left + i]

    for j in range(size2):
        R[j] = arr[mid + 1 + j]

    i = 0
    j = 0
    k = left

    '''
        both L, R are not empty
    '''
    while i < size1 and j < size2:
        
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        
        else:
            arr[k] = R[j]
            j += 1
        
        k += 1

    '''
        if R is empty
    '''
    while i < size1:
        arr[k] = L[i]
        k += 1
        i += 1

    '''
        if L is empty
    '''
    while j < size2:
        arr[k] = R[j]
        k += 1
        j += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2

        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


def main():
    arr = [12, 11, 13, 5, 6, 7]

    merge_sort(arr, 0, len(arr) - 1)

    print(arr)


if __name__ == '__main__':
    main()