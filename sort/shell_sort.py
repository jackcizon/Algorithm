'''
    why call 'shell'?

    Shell sort is named after its inventor, 
    Donald Shell, who first proposed the algorithm in 1959.
'''
import random
import time


def insert_sort_gap(arr, gap):
    for i in range(gap, len(arr)):
        key = arr[i]
        j = i - gap
        while j >= 0 and arr[j] > key:
            arr[j + gap] = arr[j]
            j -= gap
        arr[j + gap] = key

def shell_sort(arr):
    gap = len(arr) // 2
    while gap >= 1:
        insert_sort_gap(arr, gap)
        gap //= 2

# def shell_sort(arr, div):
#     n = len(arr)
#     gap = n // div
#     while gap > 0:
#         for i in range(gap, n):
#             key = arr[i]
#             #start from 0 to grap
#             j = i - gap
#             while j >= 0 and arr[j] > key:
#                 arr[j + gap] = arr[j]
#                 j -= gap
#             #arr[j - gap + gap] = key
#             arr[j + gap] = key
#         gap //= div


def main():
    arr = [i for i in range(100000, -1, -1)]
    start_time = time.time()
    
    # shell_sort([8, 3, 1, 5, 6, 4, 7, 2], 2)   
    shell_sort(arr)

    print('run time: ', time.time() - start_time)

if __name__ == '__main__':
    main() 

# '''
# \          \ 
#  \    +gap  \ 
#   \   ===>>  \ 
#    \          \ 
#     \          \ 

# divided by div
# \   \ 
#  \   \     +gap//div
#   \   \    
#    \   \ 

#    .....
#    .....
# final
# gap = 1, and compare adjacent element
# \\
#  \\
#   \\
#    \\
#    ......
#             \\

#     sort over.
# ''' 
