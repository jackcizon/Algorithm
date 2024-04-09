import random
import heapq

class MaxHeap:
    def __init__(self, heap):
        self.heap = heap
        self.build_max_heap()

    def get_left_child(self, parent):
        return 2 * parent + 1

    def get_right_child(self, parent):
        return 2 * parent + 2

    def max_heapify(self, end, start):
        left = self.get_left_child(start)
        right = self.get_right_child(start)
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
        heap_size = len(self.heap)

        # heap_size - 1 pointer to the last child, we get its parent, and max_heapify
        for i in range((heap_size - 1) // 2, -1, -1):
            self.max_heapify(heap_size, i)

    def extract_max(self):
        if len(self.heap) == 0:
            return None

        self.build_max_heap()

        max_ele = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]

        self.max_heapify(len(self.heap) - 1, 0)

        return max_ele

    def heap_push(self, val):
        self.heap.append(val)

        self.build_max_heap()


    def heap_sort(self):
        self.build_max_heap()
        last_index = len(self.heap) - 1
        end = len(self.heap) - 1

        # start from the last node and stop to the first node(we know it is smallest)
        for i in range(last_index, 0, -1):
            self.heap[0], self.heap[i] = self.heap[i], self.heap[0]
            # for each heapify, we throw a value from the last(not consider)
            end -= 1
            self.max_heapify(end, 0)

unsorted_arr = [i for i in range(10)]
random.shuffle(unsorted_arr)
print(unsorted_arr)

top_k = 5
max_heap = MaxHeap(unsorted_arr)
top_k_list = []
max_heap.heap_push(1000)
for _ in range(top_k):
    top_k_list.append(max_heap.extract_max())

print(top_k_list)
