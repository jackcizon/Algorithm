'''Quick Sort
1. Set pivot val, Usually it is the leftmost or rightmost element. 
2. In order to avoid the worst case, you can select it randomly and 
then exchange the position with pivot (usually the leftmost element)

Time Complexity: O(n*log(n))
worst case: O(n**2)
'''
import random
import time
import sys
MAX_RECURSION_LIMIT = 2**20
sys.setrecursionlimit(MAX_RECURSION_LIMIT)

def partition(arr, left, right):
    # set pivot val
    pivot = arr[left]

    while left < right:
        while left < right and arr[right] >= pivot:
            right -= 1
        arr[left] = arr[right]
        
        while left < right and arr[left] <= pivot:
            left += 1
        arr[right] = arr[left]
    
    # left = right, pivot val
    arr[left] = pivot
    return left   

def _quick_sort(arr, left, right):
    # avoid worst case, Optimization part
    # if left == right:
    #     return arr[0]

    # if len(arr) == 2:
    #     arr[0] = min(arr)
    #     arr[1] = max(arr)
    #     return arr

    # if left < right:
    #     random_index = random.randint(left + 1, right)
    #     arr[0], arr[random_index] = arr[random_index], arr[0]

    # common part
    # if left < right:
    #     pivot = partition(arr, left, right)
    #     quick_sort(arr, left, pivot - 1)
    #     quick_sort(arr, pivot + 1, right)

    # final optimized version
    if left < right:
        random_index = random.randint(left, right)
        # swap position
        arr[left], arr[random_index] = arr[random_index], arr[left]

        pivot = partition(arr, left, right)
        _quick_sort(arr, left, pivot - 1)
        _quick_sort(arr, pivot + 1, right)

def quick_sort(arr):
    _quick_sort(arr, 0, len(arr) - 1)


def main():
    worst_case_arr = [i for i in range(100000, -1, -1)]
    start_time = time.time()
    
    # quick_sort(worst_case_arr, 0, len(worst_case_arr) - 1)
    quick_sort(worst_case_arr)
    print('run time: ', time.time() - start_time)

if __name__ == '__main__':
    main() 
