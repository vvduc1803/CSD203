class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head is None
    def clear(self):
        self.head = None
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def pop(self):
        if self.isEmpty():
            return Exception("Empty")
        else:
            temp = self.head
            self.head = self.head.next
            popped = temp.data
            del temp
            return popped
    def top(self):
        if self.isEmpty():
            return Exception("Empty")
        return self.head.data
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end = " ")
            current = current.next
        print()
        
    def decimalToBinary(self, num):
        binary_stack = Stack()
        while num > 0:
            remainder = num % 2
            binary_stack.push(remainder)
            num = num // 2
        binary_num = ""
        while not binary_stack.isEmpty():
            binary_num += str(binary_stack.pop())
        return binary_num
        
s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.traverse()
s.clear()
s.traverse()
s.push(1)
s.push(2)
s.push(3)
s.traverse()
print (s.decimalToBinary(42))
