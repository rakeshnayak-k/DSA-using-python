# BST constructor

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is  None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    def __r_contains(self, current_node, value):
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __delete_node(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None 
        

        return current_node
    





bst = BinarySearchTree()
# bst.insert(47)
# bst.insert(21)
# bst.insert(76)
# bst.insert(18)
# bst.insert(27)
# bst.insert(52)
# bst.insert(82)

# print(bst.r_contains(18))

# print(bst.r_contains(17))

bst.r_insert(2)
bst.r_insert(1)
bst.r_insert(3)

print(bst.root.value)
print(bst.root.left.value)
print(bst.root.right.value)



