'''
    max heap implement:
    if not empty:
        build max heap
        swap arr[0] and arr[size-1]
        
    min heap implement:
    if not empty:
        build min heap
        new list[i] = pop arr[i from 0 to size-1]

    pop():
        new_list.append(pop(arr[0]))
        swap(arr[0], arr[size-1])
        size -= 1
        min_heap(arr, 0)
'''



def max_heapify(arr, size, i):
    l = 2 * i + 1
    r = 2 * i + 2

    _max = i

    if l < size and arr[l] > arr[_max]:
        _max = l

    if r < size and arr[r] > arr[_max]:
        _max = r

    if _max != i:
        arr[i], arr[_max] = arr[_max], arr[i]
        max_heapify(arr, size, _max)


def build_max_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        max_heapify(arr, len(arr), i)


def heap_sort(arr):
    build_max_heap(arr)
    size = len(arr) - 1
    l = len(arr) - 1
    for i in range(size, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        l -= 1
        max_heapify(arr, l, 0)
    print(arr)

def main():

    arr = [3, 5, 2, -99, 133, 789, 0, 1, 56, 1, 7, 9, 6]

    heap_sort(arr)




if __name__ == '__main__':
    main()



#Kth-row, len(heap) = 2**k, and the last item location is index(2**k - 1)

#(K+1)-row, len(heap) = 2**(k+1), and the last item location is len(heap)-1 == index(2**(k+1) - 1)

#if row(heap) == k+1, then we start from the last parent, which locate at i == index(2**k - 1)

#and i = floor(len(heap)-1)//2,

#if a heap is triple heap, 

#then we loop from size//3, to 1
