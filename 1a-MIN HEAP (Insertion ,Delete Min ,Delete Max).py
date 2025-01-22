class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def delete_max(self):
        if len(self.heap) == 0:
            return None

        # Linear scan to find max in a MinHeap
        max_index = 0
        for i in range(len(self.heap)):
            if self.heap[i] > self.heap[max_index]:
                max_index = i

        max_value = self.heap[max_index]
        # Swap max value with the last element and pop it
        self.heap[max_index] = self.heap.pop()
        if max_index < len(self.heap):  # Reheapify if not the last element
            self._heapify_down(max_index)
        return max_value

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index
            parent_index = (index - 1) // 2

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
            smallest = right_child_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

# Example Usage
min_heap = MinHeap()
values = [int(input(f"Enter value {i+1}: ")) for i in range(5)]
for value in values:
    min_heap.insert(value)

print("Values in 'min_heap':", min_heap.heap)
print("Min Heap:", min_heap.heap)
print("Delete Min:", min_heap.delete_min())
print("Min Heap after Delete Min:", min_heap.heap)
print("Delete Max:", min_heap.delete_max())
print("Min Heap after Delete Max:", min_heap.heap)
