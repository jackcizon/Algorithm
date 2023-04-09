def _max(arr, left, right):
    if left == right:
        return arr[left]
    mid = (left + right) // 2
    max_left = _max(arr, left, mid)
    max_right = _max(arr, mid + 1, right)

    return max(max_left, max_right)


arr = [1, 5, 8, 7, 3, 5, 9, 4]
print(_max(arr, 0, len(arr) - 1))
