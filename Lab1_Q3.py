class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def isEmpty(self):
        if self.head is None:
            return True
        return False
#1
    def addToHead(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
#2
    def addToTail(self, x):
        new_node = Node(x)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
#3
    def addAfter(self, position, value):
        temp = self.head
        count = 0
        while temp is not None:
            if count == position - 1:
                break
            count += 1
            temp = temp.next
        if position == 1:
            self.addToHead(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linked list. Cannot insert at {} position.".format(position,
                                                                                                             position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node = Node(value)
            new_node.next = temp.next
            new_node.previous = temp
            temp.next.previous = new_node
            temp.next = new_node
#4
    def traverse(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()
#5
    def deleteFromHead(self):
        if self.head is None:
            return None
        data = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.length -= 1
        return data
#6
    def deleteFromTail(self):
        if self.tail is None:
            return None
        data = self.tail.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return data
#7
    def deleteAfter(self, value):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            if self.head.data == value:
                self.head = None
        else:
            temp = self.head
            while temp is not None:
                if temp.data == value:
                    break
                temp = temp.next
            if temp is None:
                print("Element not present in linked list. Cannot delete element.")
            elif temp.next is None:
                self.deleteFromLast()
            else:
                temp.next = temp.next.next
                temp.next.prev = temp.prev
#8
    def delete(self, x):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == x:
                if curr_node == self.head:
                    return self.deleteFromHead()
                elif curr_node == self.tail:
                    return self.deleteFromTail()
                else:
                    curr_node.prev.next = curr_node.next
                    curr_node.next.prev = curr_node.prev
                    self.length -= 1
                    return curr_node.data
            curr_node = curr_node.next
        return None
#9
    def search(self, x):
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == x:
                return curr_node
            curr_node = curr_node.next
        return None
#10
    def count(self):
        return self.length
#11
    def delAt(self, i):
        node = self.head
        count = 0
        while node != None and count < i:
            count += 1
            node = node.next
        if node == None:
            return None
        elif node == self.head:
            return self.deleteFromHead()
        elif node == self.tail:
            return self.deleteFromTail()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            return node.data

#12
    def sort(self):
        if self.head is None:
            return
        else:
            for i in range(self.length):
                curr_node = self.head
                for j in range(i, self.length):
                    if curr_node.next is None:
                        break
                    if curr_node.data > curr_node.next.data:
                        temp = curr_node.data
                        curr_node.data = curr_node.next.data
                        curr_node.next.data = temp
                    curr_node = curr_node.next
#14
    def toArray(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.data)
            current = current.next
        return lst
    

#18    
    def max(self):
        if self.head is None:
            return None
        current = self.head
        maxVal = current.data
        while current:
            if current.data > maxVal:
                maxVal = current.data
            current = current.next
        return maxVal
#19    
    def min(self):
        if self.head is None:
            return None
        current = self.head
        minVal = current.data
        while current:
            if current.data < minVal:
                minVal = current.data
            current = current.next
        return minVal
#20    
    def sum(self):
        current = self.head
        total = 0
        while current:
            total += current.data
            current = current.next
        return total
#21    
    def avg(self):
        if not self.head:
            return 0
        n = 1
        current = self.head
        s = current.data
        current = current.next
        while current != None:
            s += current.data
            n += 1
            current = current.next
        return s/n
#22    
    def sorted(self):
        if self.head is None:
            return True
        current = self.head
        while current.next:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
#23    
    def insert(self, x):
        newNode = Node(x)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        current = self.head
        while current and current.data <= x:
            current = current.next
        
        if current is None:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        elif current.prev is None:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        else:
            newNode.prev = current.prev
            newNode.next = current
            current.prev.next = newNode
            current.prev = newNode
#24    
    def reverse(self):
        current = self.head
        
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
            
        if temp:
            self.head = temp.prev

# create a new doubly linked list
dll = DoublyLinkedList()

# add some nodes to the head and tail
dll.addToHead(1)
dll.addToTail(2)
dll.addToHead(0)
dll.addToTail(3)
dll.addToTail(4)
dll.addToTail(5)
dll.addToTail(6)
dll.addToTail(7)
dll.addToTail(8)
dll.addToTail(9)
dll.addToTail(10)
dll.addToTail(11)
dll.addToTail(12)
dll.traverse()

dll.addAfter(4, 24)
dll.traverse()  
# delete some nodes
dll.deleteFromHead()
dll.traverse()
dll.deleteFromTail()
dll.traverse()
dll.deleteAfter(7)
dll.traverse()
dll.delete(7)
dll.traverse()
# search for a node
node = dll.search(2)
print(node.data)

count = dll.count()
print(count)  

dll.delAt(5)
dll.traverse()
# sort the list
dll.sort()
dll.traverse()  

print(dll.toArray())

print(dll.max())
print(dll.min())
print(dll.sum())
print(dll.avg())
print(dll.sorted())

dll.insert(16)
dll.traverse()

dll.reverse()
dll.traverse()  
