#slectsort init an array to a unsorted,
#divide array into two part : sorted in left and unsorted in right
#then loop and compare then set order

'''Select Sort
1. Similar to bubble sort, the list is divided into ordered 
area and unordered area. 
2. Define the starting element as the minimum element in each pass, 
obtain the index value and temporarily store it. 
3. Compare adjacent elements in each pass, and change the minimum 
index value if the conditions are met. 
4. After each pass, the capacity of the unordered area is reduced by one, 
and the capacity of the ordered area is increased by 1, and it is 
judged whether the minimum index value changes. If it changes, 
exchange it
5. each pass get a min value

Time Complexity: O(n**2)
'''
def select_sort(arr):
    # total passes
    for i in range(len(arr) - 1):
        # define min value's index
        min_index = i
        # compare
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                # change min value's index
                min_index = j

        # if index chnaged, swap
        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr   

arr = select_sort([4, 7, 3, 1, 9, 0, 2])
print(arr)
