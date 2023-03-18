def linear_search(arr, val):
    for i in range(len(arr)):
        if arr[i] == val:
            print("find {}".format(val))
            return True
    print("not find {}".format(val))
    return False

arr = [1, 2, 4, 6, 0, 4]

linear_search(arr, 0)