#slectsort init an array to a unsorted,
#divide array into two part : sorted in left and unsorted in right
#then loop and compare then set order

def select_sort(arr):
    for i in range(len(arr) - 1):
        min_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    
    print(arr)      

arr = [4, 7, 3, 1, 9, 0, 2]

select_sort(arr)


'''
    In Python, you can get the length of a list 
    using the len function. 
    This works because a list in Python 
    is a dynamic data structure that stores 
    the length of the list as part of its internal 
    representation. Therefore, when you pass a list
    to a function, 
    you can use len to get its length.
'''

'''
    The arr parameter is a list, and you can use 
    len(arr) to get its length.

    In C, on the other hand, an array is a 
    fixed-size data structure that does not
    store its length as part of its
    internal representation. 
    When you pass an array to a function, 
    it decays into a pointer to its first element, 
    and the size information is lost. 
    Therefore, you cannot use sizeof(arr) / sizeof(arr[0]) 
    to get the length of the array inside the function.

    To get around this, you need to pass 
    the length of the array as a separate parameter 
    to the function
'''

