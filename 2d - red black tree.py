RED = True
BLACK = False

class Node:
    def __init__(self, key, color=RED):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = color


class RedBlackTree:
    def __init__(self):
        self.nil = Node(None, color=BLACK)
        self.nil.left = self.nil
        self.nil.right = self.nil
        self.nil.parent = self.nil
        self.root = self.nil

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.nil:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, y):
        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.parent = y
        x.parent = y.parent
        if y.parent == self.nil:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x
        x.right = y
        y.parent = x

    def insert(self, key):
        new_node = Node(key)
        y = self.nil
        x = self.root
        while x != self.nil:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right
        new_node.parent = y
        if y == self.nil:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = RED
        self.insert_fixup(new_node)

    def insert_fixup(self, z):
        while z.parent.color == RED:
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.left_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == RED:
                    z.parent.color = BLACK
                    y.color = BLACK
                    z.parent.parent.color = RED
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.right_rotate(z)
                    z.parent.color = BLACK
                    z.parent.parent.color = RED
                    self.left_rotate(z.parent.parent)
        self.root.color = BLACK

    def transplant(self, u, v):
        if u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def minimum(self, x):
        while x.left != self.nil:
            x = x.left
        return x

    def delete_node(self, z):
        y = z
        y_original_color = y.color
        if z.left == self.nil:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.nil:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == BLACK:
            self.delete_fixup(x)

    def delete_fixup(self, x):
        while x != self.root and x.color == BLACK:
            if x == x.parent.left:
                w = x.parent.right
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.left_rotate(x.parent)
                    w = x.parent.right
                if w.left.color == BLACK and w.right.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.right.color == BLACK:
                        w.left.color = BLACK
                        w.color = RED
                        self.right_rotate(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.right.color = BLACK
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == RED:
                    w.color = BLACK
                    x.parent.color = RED
                    self.right_rotate(x.parent)
                    w = x.parent.left
                if w.right.color == BLACK and w.left.color == BLACK:
                    w.color = RED
                    x = x.parent
                else:
                    if w.left.color == BLACK:
                        w.right.color = BLACK
                        w.color = RED
                        self.left_rotate(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = BLACK
                    w.left.color = BLACK
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = BLACK

    def search(self, key):
        return self.search_recursive(self.root, key)

    def search_recursive(self, node, key):
        if node == self.nil or key == node.key:
            return node
        if key < node.key:
            return self.search_recursive(node.left, key)
        return self.search_recursive(node.right, key)

    def inorder_traversal(self, node):
        if node != self.nil:
            self.inorder_traversal(node.left)
            print(node.key, end=' ')
            self.inorder_traversal(node.right)


# Test the Red-Black Tree implementation
rb_tree = RedBlackTree()
rb_tree.insert(10)
rb_tree.insert(20)
rb_tree.insert(30)
rb_tree.insert(40)
rb_tree.insert(50)
rb_tree.insert(15)
rb_tree.insert(25)

print("Inorder traversal of Red-Black Tree:")
rb_tree.inorder_traversal(rb_tree.root)
print()

# Delete a node and show the updated tree
rb_tree.delete_node(rb_tree.search(20))
print("Inorder traversal of Red-Black Tree after deletion of 20:")
rb_tree.inorder_traversal(rb_tree.root)
print()

# Search for a node
search_key = 30
if rb_tree.search(search_key) != rb_tree.nil:
    print(f"{search_key} found in Red-Black Tree.")
else:
    print(f"{search_key} not found in Red-Black Tree.")


Output:
When you run this code, it will:

Insert nodes into the Red-Black Tree.
Perform an in-order traversal to print the keys.
Delete the node with the key 20.
Perform another in-order traversal after deletion.
Search for the key 30 and print whether it is found or not.
