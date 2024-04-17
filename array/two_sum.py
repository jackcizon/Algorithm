'''Two Sum

Get a tuple whose sum of two numbers in the array
is the required sum

naive approach:
    time complexity: O(n**2)

quick sort approach:
    time complexity: O(nlog(n))
'''

import random


def naive_two_sum(size: int, sum: int) -> list:
    arr = [random.randint(1, 100) for _ in range(size)] 
    print('array :> ', arr)

    res_list = []

    for i in range(size - 1):
        for j in range(i + 1, size):
            if arr[i] + arr[j] == sum:
                res: tuple = arr[i], arr[j]
                res_list.append(res)               
    return res_list


def sort_two_sum(size: int, sum: int) -> list:
    arr = [random.randint(1, 100) for _ in range(size)]

    quick_sort(arr)
    print('sorted array :>', arr)

    res_list = []

    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] + arr[right] == sum:
            res: tuple = arr[left], arr[right]
            res_list.append(res)
            left += 1
            right -= 1

            # skip deuplicate elements
            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif arr[left] + arr[right] < sum:
            left += 1
        else:
            right -= 1

    return res_list


def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def _quick_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        random_index = random.randint(left, right)
        # swap position
        arr[left], arr[random_index] = arr[random_index], arr[left]

        pivot = partition(arr, left, right)
        _quick_sort(arr, left, pivot - 1)
        _quick_sort(arr, pivot + 1, right)


def partition(arr, left, right):
    pivot = arr[left]

    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]

    arr[left] = pivot    
    return left


if __name__ == '__main__':
    # print('naive approach :> ')
    # print('result: ', naive_two_sum(50, 100))
    print('quick sort approach :>')
    print('result: ', sort_two_sum(50, 100))
