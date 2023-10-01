from heap_sort import MaxHeap

class PriorityQueue(MaxHeap):
    def __init__(self, heap):
        super().__init__(heap)

    def heap_maximum(self):
        return self.heap[0]

    def heap_extract_max(self):
        if len(self.heap) < 1:
            raise Exception("Heap underflow: The heap is empty.")
        max_val = self.heap[0]
        self.heap[0] = self.heap[-1] # use last element to cover heap[0]
        self.heap.pop() # heap_size - 1
        self.max_heapify(len(self.heap), 0)
        return max_val

    def heap_increase_key(self, i, key):
        if key < self.heap[i]:
            raise ValueError("New key is smaller than the current key.")
        self.heap[i] = key
        while i > 0 and self.heap[i] > self.heap[(i - 1) // 2]:
            self.heap[i], self.heap[(i - 1) // 2] = self.heap[(i - 1) // 2], self.heap[i]
            i = (i - 1) // 2

    def max_heap_insert(self, key):
        self.heap.append(float("-inf"))  # Add a new element with negative infinity
        self.heap_increase_key(len(self.heap) - 1, key)

def main():
    pq = PriorityQueue([])
    pq.max_heap_insert(5)
    pq.max_heap_insert(10)
    pq.max_heap_insert(3)
    pq.max_heap_insert(7)
    print("Maximum:", pq.heap_maximum())  # Should print 10
    print("Extracted Max:", pq.heap_extract_max())  # Should print 10
    print("Maximum after extraction:", pq.heap_maximum())  # Should print 7

if __name__ == '__main__':
    main()


