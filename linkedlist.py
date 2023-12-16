# create a separate class to construct a Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None

class SingleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
    def print_llist(self):
        temp = self.head
        if self.length == 0:
            print('Empty SLL')
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    # insert a node at the end
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length+=1
        return True
    
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next 
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.tail = None
        return temp.value     

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head      
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            # print('index value ' , temp)
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
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        prev = self.get(index - 1)
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after
            
        
        





                    
# print(ll.length)
# print(ll.head.value)
# print(ll.tail.value)
        
ll = SingleLinkedList(0)
ll.append(1)
ll.append(2)
ll.append(3)

# ll.set_value(1,10)
# ll.insert_value(3,10)

# ll.remove(2)
ll.reverse()

ll.print_llist()
print(ll.get(0).value)


ll.print_llist()

# print('pop ',ll.pop_first())
# print('pop ',ll.pop())

# ll.print_llist()

        