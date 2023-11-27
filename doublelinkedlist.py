# create a separate class to construct a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_llist(self):
        temp = self.head
        if self.length == 0:
            print('Empty DLL')
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = None
            self.tail = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length/2:      
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert_value(self, index, value):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index -1)
        after = before.next

        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.prev = new_node
        
        self.length +=1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None
       
        self.length -= 1
        return temp


    

dll = DoubleLinkedList(0)
dll.append(1)
dll.append(2)
dll.append(3)

# dll.prepend(-1)
# dll.set_value(1,20)
# dll.insert_value(1,20)
# print(dll.remove(10))

dll.print_llist()

# # 2 items
# print(dll.pop())
# # 1 item
# print(dll.pop())
# # 0 item
# print(dll.pop())

# # 2 items
# print(dll.pop_first())
# # 1 item
# print(dll.pop_first())
# # 0 item
# print(dll.pop_first())

# print(dll.get(1))
# print(dll.get(2))
