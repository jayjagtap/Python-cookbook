class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self,val):
        self.root = Node(val)

    def insert(self, val):
        # if root is None
        if self.root == None:
            self.root = Node(val)
        
        # Traverse to the end node
        curr = self.root
        while curr.next != None:
            curr = curr.next
        
        curr.next = Node(val)
    
    def print_linked_list(self):

        curr = self.root
        while curr != None:
            print(f"{curr.val}")
            curr = curr.next

    def reverse_list(self):

        prev, curr = None, self.root
    
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        self.root = prev

    def delete_Node(self, val):

        # If node needs deletion is root
        if self.root.val == val:
            head = self.root
            self.root = self.root.next
            del head
            return

        prev, curr = None, self.root

        while curr.val != val and curr != None:
            prev = curr
            curr = curr.next

        prev.next = curr.next
        del curr

if __name__ == "__main__":
    my_list = LinkedList(19)
    my_list.insert(1)
    my_list.insert(2)
    my_list.insert(5)
    my_list.print_linked_list()
    my_list.reverse_list()
    print("Reversed list: ")
    my_list.print_linked_list()
    my_list.delete_Node(5)
    my_list.delete_Node(1)
    print("Print Linked List after Deletion")
    my_list.print_linked_list()
