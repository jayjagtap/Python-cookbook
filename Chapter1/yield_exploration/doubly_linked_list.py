class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class dll:
    def __init__(self, val):
        self.root = Node(val)
    
    def insert(self, val):
        # Check if root is present

        if self.root == None:
            self.root = Node(val)
            return
        
        #Traverse to the end node.
        curr = self.root
        while curr.next != None:
            curr = curr.next

        curr.next = Node(val)
        curr.next.prev = curr
    
    def reverse(self):

        if self.root == None: return None

        prev, curr = None, self.root

        while curr != None:
            nextNode = curr.next
            curr.next = prev
            curr.prev = nextNode
            prev = curr
            curr = nextNode

        self.root = prev

    def print_list(self):
        print("Printing the list")
        if self.root == None: return None

        curr = self.root
        while curr != None:
            print(curr.val)
            curr = curr.next
            
if __name__ == "__main__":
    my_dll = dll(10)
    my_dll.insert(1)
    my_dll.insert(2)
    my_dll.insert(3)
    my_dll.insert(4)
    my_dll.insert(5)
    my_dll.print_list()
    print("Reverse a list")
    my_dll.reverse()
    my_dll.print_list()