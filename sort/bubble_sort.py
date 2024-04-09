'''Bubble Sort
1. The list is divided into ordered area and unordered area. 
2. For every two adjacent numbers in the list, if the former is larger than the latter, swap the two numbers. 
3. After one sorting pass is completed, the number of unordered areas is reduced by one and the number of ordered areas is increased by one.
4. Starting from the area with index 0, the number of each trip is reduced by one.
'''
def bubble_sort(array):
    # Total number of passes. 
    for i in range(len(array) - 1):
        # The capacity of the unsorted area is reduced by one for each pass
        for j in range(len(array) - 1 - i):
    
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = bubble_sort([3, 1, 7, 8, 0, 5])
print(array)

    