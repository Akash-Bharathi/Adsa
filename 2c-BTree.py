class BTreeNode:
    def __init__(self, keys=[], children=[], is_leaf=True, max_keys=4):
        self.keys = keys
        self.children = children
        self.is_leaf = is_leaf
        self.max_keys = max_keys if max_keys else 4


class BTree:
    def __init__(self, max_keys=4):
        self.root = BTreeNode(max_keys=max_keys)

    def search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            return node, i
        if node.is_leaf:
            return None, None
        return self.search(node.children[i], key)

    def insert(self, key):
        root = self.root
        if len(root.keys) == root.max_keys:
            new_root = BTreeNode(keys=[root.keys.pop(len(root.keys)//2)], children=[root])
            self.split_child(new_root, 0)
            self.root = new_root
            root = new_root
        self.insert_non_full(root, key)

    def insert_non_full(self, node, key):
        i = len(node.keys) - 1
        if node.is_leaf:
            node.keys.append(None)
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == node.children[i].max_keys:
                self.split_child(node, i)
            if key > node.keys[i]:
                i += 1
            self.insert_non_full(node.children[i], key)

    def split_child(self, parent, i):
        node_to_split = parent.children[i]
        new_node = BTreeNode(max_keys=node_to_split.max_keys, is_leaf=node_to_split.is_leaf)
        parent.keys.insert(i, node_to_split.keys[len(node_to_split.keys)//2])
        parent.children.insert(i+1, new_node)
        new_node.keys = node_to_split.keys[len(node_to_split.keys)//2+1:]
        node_to_split.keys = node_to_split.keys[:len(node_to_split.keys)//2]
        if not node_to_split.is_leaf:
            new_node.children = node_to_split.children[len(node_to_split.keys)+1:]
            node_to_split.children = node_to_split.children[:len(node_to_split.keys)+1]

    def delete(self, key):
        self.delete_recursive(self.root, key)

    def delete_recursive(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and key == node.keys[i]:
            if node.is_leaf:
                del node.keys[i]
            else:
                if len(node.children[i].keys) >= node.max_keys/2:
                    pred = self.get_predecessor(node, i)
                    node.keys[i] = pred.keys.pop()
                elif len(node.children[i+1].keys) >= node.max_keys/2:
                    succ = self.get_successor(node, i)
                    node.keys[i] = succ.keys.pop(0)
                else:
                    self.merge(node, i)
                self.delete_recursive(node.children[i], key)
        elif node.is_leaf:
            return
        elif len(node.children[i].keys) == node.max_keys/2:
            self.fix_borrow_or_merge(node, i)
            self.delete_recursive(node.children[i], key)

    def get_predecessor(self, node, i):
        curr = node.children[i]
        while not curr.is_leaf:
            curr = curr.children[-1]
        return curr

    def get_successor(self, node, i):
        curr = node.children[i+1]
        while not curr.is_leaf:
            curr = curr.children[0]
        return curr

    def merge(self, node, i):
        child = node.children[i]
        sibling = node.children[i+1]
        child.keys.append(node.keys[i])
        child.keys += sibling.keys
        if not child.is_leaf:
            child.children += sibling.children
        del node.keys[i]
        del node.children[i+1]

    def fix_borrow_or_merge(self, node, i):
        if i > 0 and len(node.children[i-1].keys) > node.max_keys/2:
            left_sibling = node.children[i-1]
            child = node.children[i]
            if child.is_leaf:
                child.keys.insert(0, node.keys[i-1])
                node.keys[i-1] = left_sibling.keys.pop()
            else:
                child.keys.insert(0, node.keys[i-1])
                node.keys[i-1] = left_sibling.keys.pop(-1)
                child.children.insert(0, left_sibling.children.pop(-1))
        elif i < len(node.children) - 1 and len(node.children[i+1].keys) > node.max_keys/2:
            right_sibling = node.children[i+1]
            child = node.children[i]
            if child.is_leaf:
                child.keys.append(node.keys[i])
                node.keys[i] = right_sibling.keys.pop(0)
            else:
                child.keys.append(node.keys[i])
                node.keys[i] = right_sibling.keys.pop(0)
                child.children.append(right_sibling.children.pop(0))
        else:
            if i > 0:
                self.merge(node, i-1)
                del node.keys[i-1]
            else:
                self.merge(node, i)
                del node.keys[i]

    def inorder_traversal(self, node):
        if node:
            i = 0
            while i < len(node.keys):
                self.inorder_traversal(node.children[i])
                print(node.keys[i], end=' ')
                i += 1
            self.inorder_traversal(node.children[i])


# Test the B-Tree implementation
btree = BTree()
btree.insert(10)
btree.insert(20)
btree.insert(5)
btree.insert(6)
btree.insert(12)
btree.insert(30)
btree.insert(7)
btree.insert(17)

print("Inorder traversal of B-Tree:")
btree.inorder_traversal(btree.root)
print()

btree.delete(12)
print("Inorder traversal of B-Tree after deletion of 12:")
btree.inorder_traversal(btree.root)
print()

search_key = 17
node, idx = btree.search(btree.root, search_key)
if node:
    print(f"{search_key} found in B-Tree.")
else:
    print(f"{search_key} not found in B-Tree.")

Output Example:
Inorder traversal of the B-tree before and after deleting a node (12).
Search for the key 17 and output whether it's found in the B-tree.