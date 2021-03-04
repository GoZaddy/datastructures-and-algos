class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.preorder_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        all_nodes = self.preorder_print(self.root)
        return '-'.join(all_nodes)

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        all_nodes = self.preorder_print(start)
        if str(find_val) in all_nodes:
            return True
        return False

    def preorder_print(self, start):
        result = []
        result.append(str(start.value))
        while True:
            if start.left is None and start.right is None:
                return result
            else:
                res = self.preorder_print(start.left)
                for i in res:
                    result.append(i)
                
                res = self.preorder_print(start.right)
                for i in res:
                    result.append(i)
                return result
        return result
                


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.right.left = Node(4)
tree.root.right.right = Node(5)
tree.root.left.left = Node(6)
tree.root.left.right = Node(7)
tree.root.left.right.left = Node(8)
tree.root.left.right.right = Node(9)
tree.root.left.left.left = Node(10)
tree.root.left.left.right = Node(11)

a = tree.print_tree()
print(a) # 1-2-6-10-11-7-8-9-3-4-5

is_in_tree = tree.search(5)
print(is_in_tree) # True






