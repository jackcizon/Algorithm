def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j] 
            j = j - 1
            
        arr[j + 1] = key

    print(arr) 

arr = [6, 4, 3, 7, 5, 4 ,8]

#insert_sort(arr)


'''
Array is divided into sorted and unsorted parts.The left side is the sorted part, 
and from small to large, select the first element in the unsorted part, and compare 
it with the maximum value of the sorted element on the left. If it is greater than 
the value on the left, the next increment is performed.Note that the left side is a 
sorted state from small to large, so if the key (the unsorted first element) is less 
than the j value on the left (the maximum value on the left), then we shift the maximum 
value on the left one position to the right and decrement j value, let the second 
largest element on the left be compared with the key value, and so on. If the key value 
is really small, even smaller than the smallest sorted element on the left, then the 
j value has decreased to -1 at this time, and all The elements on the left have been 
shifted one position to the right, then let arr[j+1] or arr[0] be the key. The comparison 
ends, and the next loop is performed until the array is sorted and occupies the entire array.
'''
