class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node=Node(data)

        if self.head == None:
            self.head = new_node
            return
    
        curr_node = self.head
        while curr_node.next:
            curr_node=curr_node.next

        curr_node.next=new_node

    def print(self):
        if self.head==None:
            print("Linked List is empty")
            return
        
        curr_node = self.head
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.next

    def insert_after(self, node, data):
        if node == None:
            return
        new_node = Node(data)
        new_node.next=node.next
        node.next=new_node

    def remove(self, data):
        # if head
        curr_node = self.head
        if curr_node and curr_node.data == data:
            self.head = curr_node.next
            curr_node = None
            return
        
        prev=None
        while curr_node and curr_node.data != data:
            prev=curr_node
            curr_node = curr_node.next
        
        if curr_node is None:
            return
        
        prev.next=curr_node.next
        curr_node=None

    def len(self):
        curr_node=self.head
        count=0
        while curr_node:
            count+=1
            curr_node=curr_node.next
        
        return count


    def len_recursive(self, head):
        if head is None:
            return 0
        return 1 + self.len_recursive(head.next)

    


if __name__ == "__main__":
    ll = LinkedList()

    ll.append(10)
    ll.append(45)
    ll.append(99)
    ll.print()
    ll.insert_after(ll.head.next, 39)
    ll.print()
    ll.append(432)
    ll.append(66)
    ll.remove(99)
    ll.print()
    print(ll.len())



