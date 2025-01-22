import math

# Creating a Fibonacci tree
class FibonacciTree:
    def __init__(self, value):
        self.value = value
        self.child = []
        self.order = 0

    # Adding a tree as a child
    def add_at_end(self, t):
        self.child.append(t)
        self.order += 1


# Creating a Fibonacci heap
class FibonacciHeap:
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    # Insert a node
    def insert_node(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if self.least is None or value < self.least.value:
            self.least = new_tree
        self.count += 1

    # Get the minimum value
    def get_min(self):
        if self.least is None:
            return None
        return self.least.value

    # Extract the minimum value
    def extract_min(self):
        smallest = self.least
        if smallest is not None:
            # Add all children of the smallest tree to the root list
            for child in smallest.child:
                self.trees.append(child)

            # Remove the smallest tree from the root list
            self.trees.remove(smallest)

            # If no trees are left, set least to None
            if not self.trees:
                self.least = None
            else:
                # Recompute the least tree and consolidate
                self.least = self.trees[0]
                self.consolidate()

            self.count -= 1
            return smallest.value
        return None

    # Consolidate the heap
    def consolidate(self):
        max_order = floor_log(self.count) + 1
        aux = [None] * max_order

        while self.trees:
            x = self.trees.pop(0)
            order = x.order

            # Merge trees of the same order
            while aux[order] is not None:
                y = aux[order]
                if x.value > y.value:
                    x, y = y, x
                x.add_at_end(y)
                aux[order] = None
                order += 1

            aux[order] = x

        # Rebuild the tree list and find the new least value
        self.least = None
        for tree in aux:
            if tree is not None:
                self.trees.append(tree)
                if self.least is None or tree.value < self.least.value:
                    self.least = tree


def floor_log(x):
    return math.frexp(x)[1] - 1


# Example usage
fibonacci_heap = FibonacciHeap()
fibonacci_heap.insert_node(7)
fibonacci_heap.insert_node(3)
fibonacci_heap.insert_node(17)
fibonacci_heap.insert_node(24)

print('The minimum value of the Fibonacci heap:', fibonacci_heap.get_min())
print('The minimum value removed:', fibonacci_heap.extract_min())
print('The new minimum value of the Fibonacci heap:', fibonacci_heap.get_min())
