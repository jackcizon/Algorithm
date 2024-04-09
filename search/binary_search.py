'''manipluate sorted array
time complexity: O(log(n))
'''
def binary_search(arr, val):
    begin = 0
    end = len(arr) - 1
    while begin <= end:
        mid = (begin + end) // 2
        if arr[mid] == val:
            print("find {}".format(val))
            return True
        elif arr[mid] < val:
            begin = mid + 1
        else:
            end = mid - 1
    print("not find {}".format(val))
    return False

arr = [1, 2, 3, 8, 9, 10]

binary_search(arr, 3)
binary_search(arr, 0)
binary_search(arr, 9)
binary_search(arr, 8)