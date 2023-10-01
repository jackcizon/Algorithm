# if min-heap, just change '>' to '<'

class MaxHeap:
    def __init__(self, heap):
        self.heap = heap

    def max_heapify(self, end, start):
        left = 2 * start + 1
        right = 2 * start + 2
        # define a pointer _max to point max_value_index
        max_val_index = start

        if left < end and self.heap[left] > self.heap[max_val_index]:
            max_val_index = left

        if right < end and self.heap[right] > self.heap[max_val_index]:
            max_val_index = right

        #if pointer changed, swap and heapify the child
        if max_val_index != start:
            self.heap[start], self.heap[max_val_index] = self.heap[max_val_index], self.heap[start]
            self.max_heapify(end, max_val_index)

    def build_max_heap(self):
        for i in range(len(self.heap) // 2, -1, -1):
            self.max_heapify(len(self.heap), i)

    def heap_sort(self):
        self.build_max_heap()
        size = len(self.heap) - 1
        end = len(self.heap) - 1
        for i in range(size, -1, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            end -= 1
            self.max_heapify(end, 0)

def main():
    heap = [3, 5, 2, -99, 133, 789, 0, 1, 56, 1, 7, 9, 6]
    max_heap = MaxHeap(heap)
    max_heap.heap_sort()
    print(max_heap.heap)

if __name__ == '__main__':
    main()



'''
we do not need to build max heap from last element in array, beause all leaves are max_heap
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
                   3 <<== heap[0]
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
