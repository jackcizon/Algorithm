'''Bubble Sort
1. The list is divided into ordered area and unordered area. 
2. For every two adjacent numbers in the list, if the former is 
larger than the latter, swap the two numbers. 
3. After one sorting pass is completed, the number of unordered 
areas is reduced by one and the number of ordered areas is increased by one.
4. Starting from the area with index 0, the number of each trip is reduced by one.

Time Complexity: O(n**2)
'''
import time

def bubble_sort(array):
    # Total number of passes. 
    for i in range(len(array) - 1):
        # The capacity of the unsorted area is reduced by one for each pass
        for j in range(len(array) - 1 - i):
    
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

start_time = time.time()
array = [i for i in range(10000, -1, -1)]
bubble_sort(array)
print('run time: ', time.time() - start_time, ' sec')
    