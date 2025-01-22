class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, node, key):
        if not node:
            return AVLNode(key)

        if key < node.key:
            node.left = self.insert(node.left, key)
        else:
            node.right = self.insert(node.right, key)

        node.height = 1 + max(self.height(node.left), self.height(node.right))
        balance = self.balance(node)

        # Left Left Case
        if balance > 1 and key < node.left.key:
            return self.right_rotate(node)

        # Right Right Case
        if balance < -1 and key > node.right.key:
            return self.left_rotate(node)

        # Left Right Case
        if balance > 1 and key > node.left.key:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)

        # Right Left Case
        if balance < -1 and key < node.right.key:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)

        return node

    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left or not root.right:
                temp = root.left if root.left else root.right
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Left Left Case
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Right Right Case
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left Right Case
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right Left Case
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, root, key):
        if not root or root.key == key:
            return root
        if root.key < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.key, end=' ')
            self.inorder(root.right)

# Test the AVL Tree implementation
avl = AVLTree()
avl.root = avl.insert(avl.root, 10)
avl.root = avl.insert(avl.root, 20)
avl.root = avl.insert(avl.root, 30)
avl.root = avl.insert(avl.root, 40)
avl.root = avl.insert(avl.root, 50)
avl.root = avl.insert(avl.root, 25)

print("Inorder traversal of AVL tree:")
avl.inorder(avl.root)
print()

avl.root = avl.delete(avl.root, 20)
print("Inorder traversal of AVL tree after deletion of 20:")
avl.inorder(avl.root)
print()

search_key = 30
if avl.search(avl.root, search_key):
    print(f"{search_key} found in AVL tree.")
else:
    print(f"{search_key} not found in AVL tree.")


Output Example:
Inorder traversal of the AVL tree before and after deleting node 20.
A search operation for key 30, which checks if it's present in the tree.
