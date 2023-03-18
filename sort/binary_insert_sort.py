#two parts, left:sorted array, right: unsorted array
#find the lowest element > item
def binary_search(arr, item, high):
    low = 0
    
    while low <= high:
        mid = (int)((high + low) / 2)

        if item == arr[mid]:
            return mid + 1
        
        elif item > arr[mid]:
            low = mid + 1
        
        else:
            high = mid - 1
   
    return low

def binary_insert_sort(arr):
    for i in range(1, len(arr)):
        j = i - 1
        selected = arr[i];   

        #not use linear search, use binary only logN times
        lowest_loc_greater_than_selected = binary_search(arr, selected, j)

        while(j >= lowest_loc_greater_than_selected):
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = selected

    print(arr)

arr = [2, 4, 0, 9, 5, 7, 1]

binary_insert_sort(arr)




'''
Suppose we need to sort the following array:
8 6 1 5 3

    We assume that the first element is already sorted. 
    We take the second element and store it in a variable (key).
    Now, we use binary search to find the element on the left of the current element, which is just greater than it.
    In this case, we have only one element, 8, and it is greater than 6. So, we shift 8 one index towards the right and place 6 at its position.

The array now looks like this:
6 8 1 5 3

    Now, we take the third element, 1. Note that all the elements before the current element are sorted.
    We store 1 in key and find the element just greater than 1 in the sorted part using binary search.
    Here, the required element is 6. So, we shift 6 and 8 one index towards the right and place 1 at the position of 6 before shifting.

The array now looks like this:
1 6 8 5 3
    We now take the 4th element, 5, and store it in key.
    Using binary search, we find the element just greater than 5 in the sorted part. In this case, the required element is 6. 
    Again, we shift 6 and 8 one index towards the right and place 5 at the position of 6 before shifting.

The array now looks like this:
1 5 6 8 3
    We now take the last (5th) element, which is 3, and find the element just greater than it in the sorted part. 
    The required element is 5. We shift 5, 6, and 8 one index towards the right and place 3 at the position of 5 before shifting.

The resulting array is:
1 3 5 6 8
We have sorted the given array using binary insertion sort.
'''