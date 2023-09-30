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
数组分为已排序部分和未排序部分
左边为已排序部分，且从小到大，在未排序部分挑选第一个元素，先于左边已排序元素的最大值比较，如果大与左边的值，则进行下一次递增，
注意到左边是从小到大的已排序状态，所以如果该key（未排序的第一个元素）小于左边的j值（左边最大值），那么我们让左边最大值右移一位，
并且递减j值，让左边第二大与key值比较，以此类推，假使该key值真的很小，甚至比左边已排序的最小元素都小，那么此时j值已经递减到-1了，
且所有左边元素都已经右移一位，那么此时令arr[j+1]即arr[0]为key，比较结束，再进行下一次循环，直到数组的已排序占据整个数组。
'''
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
