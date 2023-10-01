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


def max_heapify(arr, end, start):
    left = 2 * start + 1
    right = 2 * start + 2
    # define a pointer _max to point max_value_index
    max_val_index = start

    if left < end and arr[left] > arr[max_val_index]:
        max_val_index = left

    if right < end and arr[right] > arr[max_val_index]:
        max_val_index = right

    #if pointer changed, swap and heapify the child
    if max_val_index != start:
        arr[start], arr[max_val_index] = arr[max_val_index], arr[start]
        max_heapify(arr, end, max_val_index)


def build_max_heap(arr):
    for i in range(len(arr)//2, -1, -1):
        max_heapify(arr, len(arr), i)


def heap_sort(arr):
    build_max_heap(arr)
    size = len(arr) - 1
    end = len(arr) - 1
    for i in range(size, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        end -= 1
        max_heapify(arr, end, 0)


def main():

    arr = [3, 5, 2, -99, 133, 789, 0, 1, 56, 1, 7, 9, 6]
    heap_sort(arr)
    print(arr)


if __name__ == '__main__':
    main()


'''
we do not need to build maxc heap from last element in array, beause all leaves are max_heap
and we heapify from size//2 downto 1, to ensure after all heapify can make max_heap

build_max_heap:
                  789
                /    |
             133      9
            /  |     / |
          56   7    6  0
         /|   /|   /| /|
        1 99 1 5  2 3 <<==size, end

after first sort:
                   3 <<== arr[0]
                /    |
             133        9
            /  |     /   |
          56   7    6    0
         /|   /|   /|   /|
        1 99 1 5  2 789 
                 /\\
                 ||
              new end, size

heapify, sort, etc ...

sort need n rounds, each round get a relative large_value, from largest to smallest
'''



#Kth-row, len(heap) = 2**k, and the last item location is index(2**k - 1)

#(K+1)-row, len(heap) = 2**(k+1), and the last item location is len(heap)-1 == index(2**(k+1) - 1)

#if row(heap) == k+1, then we start from the last parent, which locate at i == index(2**k - 1)

#and i = floor(len(heap)-1)//2,

#if a heap is triple heap, 

#then we loop from size//3, to 1
