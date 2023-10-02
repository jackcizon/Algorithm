from heap_sort import MaxHeap


class PriorityQueue(MaxHeap):
    def __init__(self, heap):
        super().__init__(heap)

    def heap_maximum(self):
        return self.heap[0]

    def get_heap_size(self):
        return len(self.heap)

    def heap_extract_max(self):
        if len(self.heap) < 1:
            raise Exception("Heap underflow: The heap is empty.")
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1]  # use last element to cover heap[0]
        self.heap.pop()  # heap_size - 1
        self.max_heapify(len(self.heap), 0)
        return max_val

    # similar to the priority of computer tasks. We can only increase it but not decrease it.
    def heap_increase_key(self, i, key):
        if key < self.heap[i]:
            raise ValueError("New key is smaller than the current key.")
        self.heap[i] = key
    # heapify
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def max_heap_insert(self, key):
        # Add a new element with negative infinity to expand heap, then insert element
        self.heap.append(float("-inf"))
        self.heap_increase_key(len(self.heap) - 1, key)

    def build_max_heap(self, arr):
        n = len(arr)
        for i in range(n):
            self.max_heap_insert(arr[i])


def main():
    pq = PriorityQueue([])
    pq.build_max_heap([1, 33, 4, 6, 3, 2])
    pq.max_heap_insert(5)
    pq.max_heap_insert(10)
    pq.max_heap_insert(3)
    pq.max_heap_insert(7)
    print("all tasks: {}".format(pq.heap))# this would be a max-heap
    print("Maximum:", pq.heap_maximum())  # Should print 33
    print("Extracted Max:", pq.heap_extract_max())  # Should print 33
    print("Maximum after extraction:", pq.heap_maximum())  # Should print 10
    print("after extraction, all tasks: {}".format(pq.heap))# this would be a max-heap


if __name__ == '__main__':
    main()
