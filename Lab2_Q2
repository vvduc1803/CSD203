class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linked_queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def isEmpty(self):
        return self.head is None
    def clear(self):
        self.head = None
    def enqueue(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def dequeue(self):
        if self.head is None :
            raise Exception("Empty")
        answer = self.head.data
        self.head = self.head.next
        if self.head is None :
            self.tail = None
        return answer
            
    def first(self):
        if self.head is None:
            raise Exception("Empty")
        else :
            return self.head.data
        
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next
        print()
    
    def pop(self):
        if self.isEmpty():
            return Exception("Empty")
        else:
            temp = self.head
            self.head = self.head.next
            popped = temp.data
            del temp
            return popped

def decimalToBinary(decimal):
    binary_num = ""
    max_iterations = 10
    while decimal!=0 and max_iterations > 0:
        decimal*=2
        if decimal>=1:
            binary_num+=str(1)
            decimal -=1
        else :
            binary_num+=str(0)
        max_iterations -= 1
    return binary_num

s=Linked_queue()
s.enqueue(5)
s.enqueue(2)
s.enqueue(1)
s.enqueue(9)
s.dequeue()
s.traverse()
print(decimalToBinary(0.25))



