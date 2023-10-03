def count_sort(arr):
    arr_min = min(arr)
    arr_max = max(arr)
    # output array
    b = [0] * len(arr)
    # count array
    c = [0] * (arr_max - arr_min + 1)
    for i in arr:
        # Now c[i - arr_min] records the counts of c[i - arr_min] = i
        c[i - arr_min] += 1
    for i in range(1, len(c)):
        # now c[i] records the count of elements <= (i + arr_min)
        c[i] += c[i - 1]
    '''
    for i in range(len(arr) - 1, -1, -1):
        # count index start from 0
        index = c[arr[i] - arr_min] - 1
        # e.g: index = 1, arr[i] - arr_min = 0, it stands for elements <= 1, only have 1, so we must pust that element in index 1
        b[index] = arr[i]
        # after counting a key, decrement the count
        c[arr[i] - arr_min] -= 1
    '''
    for num in reversed(arr):
        index = c[num - arr_min] - 1
        b[index] = num
        c[num - arr_min] -= 1

    for i in range(len(arr)):
        arr[i] = b[i]
    return arr


arr = [2, 5, 3, 0, 2, 3, 0, 3]
count_sort(arr)
print(arr)
