class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SinglyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
    
    def is_empty(self):
        return self.head is None
    
    def __len__(self):
        return self.size
#1    
    def addToHead(self, data):
        node=Node(data)
        node.next=self.head
        self.head=node
        self.size+=1
#2
    def addToTail(self):
        node=Node(data)
        if self.is_empty():
            self.head=node
        else:
            end_node=self.head
            while end_node.next is not None:
                end_node=end_node.next
            end_node.next=node
        self.size+=1

#3
    def addAfter(self,data,pos):
        node = Node(data)
        pre_node = self.head
        for i in range(0, pos-1):
            pre_node = pre_node.next

        post_node = pre_node.next

        pre_node.next = node
        node.next = post_node
        self.size += 1
#4
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print(end='\n')
#5    
    def deleteFromHead(self):
        if self.is_empty():
            print('Empty linked list')
        else:
            del_node=self.head
            back_node=del_node.next
            self.head=back_node
            self.size-=1
#6
    def deleteFromTail(self):
        pre_end_node = self.head
        for i in range(self.size - 2):
            pre_end_node = pre_end_node.next

        pre_end_node.next = None
        self.size -= 1
#7
    def deleteAfter(self):
        pre_node = self.head
        for i in range(pos-1):
            pre_node = pre_node.next

        node = pre_node.next
        post_node = node.next
        pre_node.next = post_node
        self.size -= 1
#8
    def delete(self,val):
        node=self.head
        for i in range(self.size-1):
            if node.data==val:
                self.deleteAfter(i)
                self.size-=1
                break
            node=node.next
#9
    def search(self,val):
        node=self.head
        for i in range(self.size-1):
            if node.data==val:
                print('Vị trí thứ',i,'có xuất hiện',val)
                break
            node=node.next
#10
    def count(self):
        print(self.size)
#11
    def delete_th(self,i):
            node=self.head
            for m in  range(self.size-1):
                if m==i-1:
                    self.deleteAfter(i-1)
                    self.size-=1
                    break
                node=node.next


#12
    def sort(self,reverse=False):
        current=self.head
        temp_list=[]
        while current is not None:
            temp_list.append(current.data)
            current=current.next
        if not reverse:
            temp_list=sorted(temp_list)
        else:
            temp_list=sorted(temp_list,reverse=True)
        self.head=None
        for data in temp_list:
            node=Node(data)
            if self.is_empty():
                self.head=node
            else:
                end_node=self.head
                while end_node.next is not None:
                    end_node=end_node.next
                end_node.next=node
#13
    def delete(self,val):
        node=self.head
        for i in range(self.size-1):
            if node.data==val:
                self.deleteAfter(i)
                self.size-=1
                break
            node=node.next
#14 (in ra như bình thường ?)
    def toArray(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next
        print(end='\n')
#15
    
#18
    def max(self):
        current = self.head
        a = self.head.data
        while current:
            if a <= current.data:
                a=current.data
            current=current.next
        return a
#19
    def min(self):
        current = self.head
        a = self.head.data
        while current:
            if a >= current.data:
                a=current.data
            current=current.next
        return a
#20
    def sum(self):
        current=self.head
        a=0
        while current:
            a= a+current.data
            current=current.next
        return a
#21
    def avg(self):
        return (self.sum()/self.count())
