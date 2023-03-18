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

insert_sort(arr)
