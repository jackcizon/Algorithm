def bubble_sort(array):
    for i in range(len(array) - 1):
    
        for j in range(len(array) - 1 - i):
    
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    
    print(array) 

array = [3, 1, 7, 8, 0, 5]

bubble_sort(array)



    