# Stack : LIFO - Last In First Out 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        if self.height == 0:
            print('Empty Stack')
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp



# stk = Stack(4)

# stk.push(2)
# stk.push(99)

# stk.print_stack()

# print('pop',stk.pop())



# Queue : FIFO - First In First Out 