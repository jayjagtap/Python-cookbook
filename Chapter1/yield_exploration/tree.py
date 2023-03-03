from collections import deque
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    
    def __init__(self, val):
        self.root = Node(val)
    
    def preorder(self, root, order=[]):
        if root == None: # reached end, return
            return
    
        order.append(root.val)
        self.preorder(root.left, order)
        self.preorder(root.right, order)

        return order
    
    def postorder(self, root, order=[]):
        if root == None: # reached end, return
            return
    
        self.postorder(root.left, order)
        self.postorder(root.right, order)
        order.append(root.val)
        
        return order
    
    def inorder(self, root, order=[]):
        if root == None: # reached end, return
            return
    
        self.inorder(root.left, order)
        order.append(root.val)
        self.inorder(root.right, order)

        return order
    
    def BFS(self, root, order=[]):
        if root == None: return []
        
        Q = deque()
        Q.append(root)

        while Q:
            front = Q.popleft()
            order.append(front.val)

            if front.left: Q.append(front.left)
            if front.right: Q.append(front.right)
        
        return order
        

if __name__ == "__main__":

    my_tree = Tree(15)
    my_tree.root.left = Node(12)
    my_tree.root.right = Node(11)
    my_tree.root.left.left = Node(16)
    my_tree.root.left.right = Node(3)
    my_tree.root.right.right = Node(8)

    print("Preorder Traversal: ", my_tree.preorder(my_tree.root))
    print("Postorder Traversal: ", my_tree.postorder(my_tree.root))
    print("Inorder Traversal: ", my_tree.inorder(my_tree.root))
    print("BFS Traversal: ", my_tree.BFS(my_tree.root))


    # Preorder Traversal:  [15, 12, 16, 3, 11, 8]
    # Postorder Traversal:  [16, 3, 12, 8, 11, 15]
    # Inorder Traversal:  [16, 12, 3, 15, 11, 8]
    # BFS Traversal:  [15, 12, 11, 16, 3, 8]
