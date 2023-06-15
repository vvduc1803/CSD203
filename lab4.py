class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

class BST:
    def __init__(self):
        self.root = None

    def visit(self, node):
        print(node.data, end=' ')

    def isEmpty(self):
        if self.root:
            return False
        else:
            return True

    def clear(self):
        self.root = None

    def search(self, x):
        if self.isEmpty():
            return False
        else:
            curr_node = self.root
            while curr_node:
                if x == curr_node.val:
                    return True
                elif x < curr_node.data:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            return False

    def insert(self, data):
        if self.isEmpty():
            self.root = Node(data)
        else:
            curr_node = self.root
            while True:
                if data == curr_node.data:
                    print('Node exist')
                    break
                elif data < curr_node.data:
                    if not curr_node.left:
                        curr_node.left = Node(data)
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if not curr_node.right:
                        curr_node.right = Node(data)
                        break
                    else:
                        curr_node = curr_node.right


    def breadth(self):
        if self.isEmpty():
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            self.visit(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def preorder_recur(self, node):
        if node:
            self.visit(node)
            self.preorder_recur(node.left)
            self.preorder_recur(node.right)

    def preorder(self):
        self.preorder_recur(self.root)

    def inorder_recur(self, node):
        if node:
            if node.left:
                self.inorder_recur(node.left)
            self.visit(node)
            if node.right:
                self.inorder_recur(node.right)

    def inorder(self):
        self.inorder_recur(self.root)

    def postorder_recur(self, node):
        if node:
            self.postorder_recur(node.left)
            self.postorder_recur(node.right)
            self.visit(node)

    def postorder(self):
        self.postorder_recur(self.root)

    def count(self):
        if self.isEmpty():
            return 0

        queue = []
        queue.append(self.root)
        total = 1

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
                total += 1
            if current_node.right:
                queue.append(current_node.right)
                total += 1
        return total

    def search_parent_child(self, x):
        if self.isEmpty():
            return 'Empty Tree', 'Empty', None

        else:
            curr_node = parent = self.root
            state = 'I'
            while curr_node.data != x:
                if x < curr_node.data:
                    parent = curr_node
                    state = 'L'
                    curr_node = curr_node.left

                if x > curr_node.data:
                    parent = curr_node
                    state = 'R'
                    curr_node = curr_node.right

                if curr_node is None:
                    state = None
                    break

            return parent, curr_node, state

    def dele(self, x):
        parent, curr_node, state = self.search_parent_child(x)
        if parent == 'Empty Tree':
            return parent

        elif state is None:
            return "Value don't exist"

        else:
            if curr_node.left is None and curr_node.right is None:
                if state == 'R':
                    parent.right = None
                else:
                    parent.left = None



            elif curr_node.left is not None:
                if state == 'R':
                    parent.right = curr_node.left
                else:
                    parent.left = curr_node.left

            else:
                if state == 'R':
                    parent.right = curr_node.right
                else:
                    parent.left = curr_node.right





    def min(self):
        if self.isEmpty():
            return None
        else:
            curr_node = self.root
            while curr_node.left:
                curr_node = curr_node.left

            return curr_node.data

    def max(self):
        if self.isEmpty():
            return None
        else:
            curr_node = self.root
            while curr_node.right:
                curr_node = curr_node.right

            return curr_node.data

    def sum(self):
        if self.isEmpty():
            return None
        queue = []
        total = self.root.data
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.left:
                queue.append(current_node.left)
                total += current_node.left.data
            if current_node.right:
                queue.append(current_node.right)
                total += current_node.right.data

        return total

    def avg(self):
        return self.sum() / self.count()





tree = BST()
tree.insert(6)
tree.insert(2)
tree.insert(8)
tree.insert(1)
tree.insert(4)
tree.insert(7)
tree.insert(9)
tree.insert(3)
tree.insert(5)
print(tree.avg())