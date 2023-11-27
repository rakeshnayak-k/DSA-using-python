# Queue : FIFO - First In First Out 

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1

    def print_queue(self):
        temp = self.first
        if self.height == 0:
            print('Empty Stack')
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.height == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1

    def dequeue(self):
        if self.height == 0:
            return None
        temp = self.first
        if self.height == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.height -= 1
        return temp



qu = Queue(0)

qu.enqueue(1)
qu.enqueue(10)

# stk.push(99)

qu.print_queue()

# 2 items
print('dequeue',qu.dequeue())
# 1 item
print('dequeue',qu.dequeue())
# 0 item
print('dequeue',qu.dequeue())
