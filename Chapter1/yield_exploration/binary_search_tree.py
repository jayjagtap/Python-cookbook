import tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class bst:
    def __init__(self, val):
        self.root = Node(val)
    
    def add_node(self, root, value):
        
        if value < root.val:
            if root.left == None: 
                root.left = Node(value) 
                return
            else: 
                self.add_node(root.left, value)
        elif value > root.val:
            if root.right == None:
                root.right = Node(value)
                return
            else:
                self.add_node(root.right, value)

    def get_min_bst(self, root):
        if root is None: return None

        if root.left == None:
            return root.val
        
        return self.get_min_bst(root.left)
    
    def get_max_bst(self, root):
        if root is None: return None

        if root.right == None:
            return root.val
        
        return self.get_max_bst(root.right)
    
    def height(self, root):
        if root == None:
            return -1
        
        return 1 + max(self.height(root.left), self.height(root.right))
    
    def is_valid_bst(self, root, min_bound=float('-inf'), max_bound=float('inf')):

        if root == None: return True
        if min_bound > root.val or max_bound < root.val:
            return False
        return self.is_valid_bst(root.left, min_bound, max_bound=root.val) and self.is_valid_bst(root.right, min_bound=root.val, max_bound=max_bound)
    
    def search_bst(self, root, value):
        if root == None: return False
        if value == root.val:
            return True
        elif value < root.val:
            return self.search_bst(root.left, value)
        else:
            return self.search_bst(root.right, value)

if __name__ == "__main__":
    my_bst = bst(15)
    my_bst.add_node(my_bst.root, 9)
    my_bst.add_node(my_bst.root, 3)
    my_bst.add_node(my_bst.root, 19)
    my_bst.add_node(my_bst.root, 16)
    my_bst.add_node(my_bst.root, 5)
    my_bst.add_node(my_bst.root, 17)
    print(tree.Tree.BFS(my_bst, root=my_bst.root)) # [15, 9, 19, 3, 16, 5, 17]

    print("Min value of bst: ", my_bst.get_min_bst(my_bst.root))
    print("Max value of bst: ", my_bst.get_max_bst(my_bst.root))
    print("Height of the tree: ", my_bst.height(my_bst.root))
    print("Is Valid: ", my_bst.is_valid_bst(my_bst.root))
    print("Search for 16: ", my_bst.search_bst(my_bst.root, value=16))
    print("Search for 18: ", my_bst.search_bst(my_bst.root, value=18))
    my_bst.root.right.left.left = Node(4)
    print("Is Valid: ", my_bst.is_valid_bst(my_bst.root))