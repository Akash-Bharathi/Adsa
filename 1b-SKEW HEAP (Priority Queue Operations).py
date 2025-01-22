class SkewNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class SkewHeap:
    def __init__(self):
        self.root = None

    def merge(self, h1, h2):
        if not h1:
            return h2
        if not h2:
            return h1

        # Ensure h1 is the smaller root
        if h1.value > h2.value:
            h1, h2 = h2, h1

        # Swap the children of h1 and recursively merge
        h1.right, h1.left = h1.left, self.merge(h1.right, h2)
        return h1

    def insert(self, value):
        new_node = SkewNode(value)
        self.root = self.merge(self.root, new_node)

    def delete_min(self):
        if not self.root:
            return None
        min_value = self.root.value
        # Merge left and right subtrees
        self.root = self.merge(self.root.left, self.root.right)
        return min_value

# Example Usage
skew_heap = SkewHeap()
skew_heap.insert(4)
skew_heap.insert(2)
skew_heap.insert(7)
skew_heap.insert(6)

print("Skew Heap root after insertion:", skew_heap.root.value)

min_val = skew_heap.delete_min()
print("Deleted Min:", min_val)
print("Skew Heap root after deletion:", skew_heap.root.value)

min_val = skew_heap.delete_min()
print("Deleted Min:", min_val)
print("Skew Heap root after deletion:", skew_heap.root.value)
