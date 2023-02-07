class Stack():
    def __init__(self):
        self.stack = []

    def push(self,element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()
    
    def peek(self):
        return self.stack[-1] if len(self.stack) else None

    def is_empty(self):
        return False if len(self.stack) else True
    
    def print(self):
        return self.stack


if __name__ == "__main__":
    my_stack = Stack()

    my_stack.push(1)
    my_stack.push(99)
    print(my_stack.print())
    print("Peek on top: ", my_stack.peek())
    my_stack.push(29)
    print(my_stack.print())
    my_stack.pop()
    print(my_stack.print())

        