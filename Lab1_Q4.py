class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
        
#1
    def addToHead(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head
            self.head = new_node
#2 
    def addToTail(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.next = self.head
#3            
    def addAfter(self, p, x):
        if not self.head:
            print("List is empty")
            return
        new_node = Node(x)
        current = self.head
        while current:
            if current.data == p:
                break
            current = current.next
            if current == self.head:
                print("Node not found in the list")
                return
        new_node.next = current.next
        current.next = new_node
#4
    def traverse(self):
        if self.head is None:
            print("List is empty")
        else:
            curr_node = self.head
            while curr_node.next != self.head:
                print(curr_node.data, end=" ")
                curr_node = curr_node.next
            print(curr_node.data)
#5
    def deleteFromHead(self):
        if self.head is None:
            return None
        curr_node = self.head
        while curr_node.next != self.head:
            curr_node = curr_node.next
        curr_node.next = self.head.next
        info = self.head.data
        self.head = self.head.next
        return info
#6
    def deleteFromTail(self):
        if self.head is None:
            return None
        curr_node = self.head
        prev_node = None
        while curr_node.next != self.head:
            prev_node = curr_node
            curr_node = curr_node.next
        info = curr_node.data
        prev_node.next = self.head
        return info
#7
    def deleteAfter(self, p):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            if current.data == p:
                break
            current = current.next
            if current == self.head:
                print("Node not found in the list")
                return
        if current.next == self.head:
            print("Cannot delete after tail node")
            return
        else:
            data = current.next.data
            current.next = current.next.next
        return data
#8     
    def delete(self, x):
        if self.head is None:
            return None
        if self.head.data == x:
            return self.deleteFromHead()
        curr_node = self.head
        prev_node = None
        while curr_node.next != self.head:
            prev_node = curr_node
            curr_node = curr_node.next
            if curr_node.data == x:
                prev_node.next = curr_node.next
                return curr_node.data
        if curr_node.data == x:
            prev_node.next = self.head
            return curr_node.data
        return None
#9 
    def search(self, x):
        if self.head is None:
            return None
        curr_node = self.head
        while curr_node.next != self.head:
            if curr_node.data == x:
                return curr_node
            curr_node = curr_node.next
        if curr_node.data == x:
            return curr_node
        return None
#10
    def count(self):
        if self.head is None:
            return 0
        count = 1
        curr_node = self.head
        while curr_node.next != self.head:
            count += 1
            curr_node = curr_node.next
        return count
#11
    def deleteAtIndex(self, i):
        if self.head is None:
            return None
        if i == 0:
            return self.deleteFromHead()
        curr_node = self.head
        prev_node = None
        curr_index = 0
        while curr_node.next != self.head:
            if curr_index == i:
                prev_node.next = curr_node.next
                return curr_node.data
            prev_node = curr_node
            curr_node = curr_node.next
            curr_index += 1
        if curr_index == i:
            prev_node.next = self.head
            return curr_node.data
        return None
#12    
    # Function to sort the list in ascending order
    def sort(self):
        if self.head is None:
            return
        else:
            current = self.head
            while current.next != self.head:
                index = current.next
                while index != self.head:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data
                    index = index.next
                current = current.next
#14 
    # Function to create an array from the linked list
    def toArray(self):
        arr = []
        if self.head is None:
            return arr
        else:
            current = self.head
            while current.next != self.head:
                arr.append(current.data)
                current = current.next
            arr.append(current.data)
            return arr 
#17
    # Function to attach a singly linked list to the end of another singly linked list
    def attachList(self, head2):
        if self.head == None:
            self.head = head2
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = head2.head
#18    
    # Function to find the maximum value in the circular linked list
    def max(self):
        if self.head == None:
            return None
        
        current = self.head
        max_val = current.data
        while current.next != self.head:
            if current.data > max_val:
                max_val = current.data
            current = current.next
        if current.data > max_val:
            max_val = current.data
        return max_val
#19 
    def min(self):
        if self.head == None:
            return None
        
        current = self.head
        min_val = current.data
        while current.next != self.head:
            if current.data < min_val:
                min_val = current.data
            current = current.next
        if current.data < min_val:
            min_val = current.data
        return min_val
#20     
    def sum(self):
        if not self.head:
            return 0
        current = self.head
        s = current.data
        current = current.next
        while current != self.head:
            s += current.data
            current = current.next
        return s
#21    
    def avg(self):
        if not self.head:
            return 0
        n = 1
        current = self.head
        s = current.data
        current = current.next
        while current != self.head:
            s += current.data
            n += 1
            current = current.next
        return s/n
#22 
    def sorted(self):
        if not self.head:
            return True
        current = self.head
        while current.next != self.head:
            if current.data > current.next.data:
                return False
            current = current.next
        return True
#23 
    def insert(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        elif self.head.data >= x:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head and current.next.data < x:
                current = current.next
            new_node.next = current.next
            current.next = new_node
#24    
    def reverse(self):
        if not self.head or not self.head.next:
            return self.head
        
        prev = None
        current = self.head
        while current.next != self.head:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        current.next = prev
        self.head.next = current
        self.head = current
# Create a new instance of the CircularLinkedList class
my_list = CircularLinkedList()

# Add elements to the list
my_list.addToHead(3)
my_list.addToTail(5)
my_list.addAfter(3, 4)
my_list.addToTail(6)
my_list.addToTail(7)
my_list.addToTail(8)
my_list.addToHead(1)
my_list.addAfter(1, 2)
my_list.addToTail(9)
my_list.addToTail(10)

my_list.traverse() 


my_list.deleteFromTail()
my_list.traverse()

my_list.deleteFromHead()
my_list.traverse()

my_list.deleteAfter(7)
my_list.deleteAfter(5)
my_list.traverse()

my_list.delete(2)
my_list.traverse()
my_list.delete(5)
my_list.traverse()
node = my_list.search(4)
print(node.data) 

# Count the number of elements in the list
count = my_list.count()
print(count) 

# Delete an element at index 0
my_list.deleteAtIndex(2)

# Print the updated contents of the list
my_list.traverse()


he_list = CircularLinkedList()
he_list.addToHead(1)
he_list.addToHead(123)
he_list.addToHead(96)
he_list.addToHead(32)
he_list.addToHead(57)
he_list.addToHead(64)
he_list.addToHead(33)
he_list.addToHead(13)
he_list.addToHead(17)
he_list.addToHead(29)
he_list.traverse()
he_list.sort()
he_list.traverse()
print(he_list.toArray())
print(he_list.max())
print(he_list.min())
print(he_list.sum())
print(he_list.avg())
print(he_list.sorted())
he_list.insert(46)
he_list.traverse()
he_list.reverse()
he_list.traverse()
