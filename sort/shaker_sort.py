# begin -> end using bubble
# end -> begin using bubble
# so only need loop length / 2
# in beginning , begin and end both sorted 
#small to right, big to left
def shaker_sort(arr):
    for i in range((int)(len(arr) / 2) + 1):

        for j in range(i, len(arr) - i - 1):
        
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        for k in range(len(arr) - 1 - i, i, -1):
            
            if arr[k] > arr[k - 1]:
                arr[k], arr[k - 1] = arr[k - 1], arr[k]

    print(arr)

shaker_sort([1, 4, 2, 3, 7, 6])

# range(start, end, steps):
'''
    steps > 0:
        start + 0 * step, start + 1 * step, ..., (not contain end)

    steps < 0:
        end - 0 * step, end - 1 * step, ..., (not contain start)
'''