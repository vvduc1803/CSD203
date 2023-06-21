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
                if x == curr_node.data:
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

        print()

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

    def dele(self, x):
        if self.isEmpty():
            return None

        parent_node = None
        node_to_delete = self.root

        # Find the node to delete and its parent
        while node_to_delete is not None and node_to_delete.data != x:
            parent_node = node_to_delete
            if x < node_to_delete.data:
                node_to_delete = node_to_delete.left
            else:
                node_to_delete = node_to_delete.right

        # If node was not found, return the original tree
        if node_to_delete is None:
            return None

        # Case 1: Node has no children
        if node_to_delete.left is None and node_to_delete.right is None:
            if parent_node is None:
                return None
            elif parent_node.left == node_to_delete:
                parent_node.left = None
            else:
                parent_node.right = None

        # Case 2: Node has one child
        elif node_to_delete.left is None:
            if parent_node is None:
                return node_to_delete.right
            elif parent_node.left == node_to_delete:
                parent_node.left = node_to_delete.right
            else:
                parent_node.right = node_to_delete.right
        elif node_to_delete.right is None:
            if parent_node is None:
                return node_to_delete.left
            elif parent_node.left == node_to_delete:
                parent_node.left = node_to_delete.left
            else:
                parent_node.right = node_to_delete.left

        # Case 3: Node has two children
        else:
            min_node_val = self.min_for_small_tree(node_to_delete.right)
            temp_val = min_node_val
            self.dele(min_node_val)
            node_to_delete.data = temp_val

    def min_for_small_tree(self, node):
        if self.isEmpty():
            return None
        else:
            curr_node = node
            while curr_node.left:
                curr_node = curr_node.left

            return curr_node.data

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

    def height_recur(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height_recur(node.left)
            right_height = self.height_recur(node.right)
            return max(left_height, right_height) + 1

    def height(self):
        return self.height_recur(self.root)

    def cost_recur(self, node):
        if node is None:
            return 0
        else:
            left_height = self.cost_recur(node.left)
            right_height = self.cost_recur(node.right)
            return max(left_height, right_height) + node.data

    def cost(self):
        return self.cost_recur(self.root)

    def isAVL_recur(self, node):
        if node is None:
            return

        height_left = self.height_recur(node.left)
        height_right = self.height_recur(node.right)

        if abs(height_right - height_left) > 1:
            return False
        else:
            self.isAVL_recur(node.left)
            self.isAVL_recur(node.right)

        return True
    def isAVL(self):
        return self.isAVL_recur(self.root)

class BT:
    def __init__(self, root_val=None):
        self.root = Node(root_val)

    def insert(self, parent_node, data, side='L' or 'R'):
        node = Node(data)
        if side == 'L':
            if parent_node.left is None:
                parent_node.left = node
            else:
                node.left = parent_node.left
                parent_node.left = node

        elif side == 'R':
            if parent_node.right is None:
                parent_node.right = node
            else:
                node.right = parent_node.right
                parent_node.right = node

        else:
            print("Side is 'L' or 'R'")


    def check_value(self, node):
        if node.left and node.right:
            if node.data > node.left.data or node.data > node.right.data:
                return False
            return True
        elif node.left:
            if node.data > node.left.data:
                return False
            return True
        elif node.right:
            return False
        else:
            return None

    def check_leaf(self, node):
        if node.left or node.right:
            return False
        return True

    def visit(self, node):
        print(node.data, end=' ')

    def breadth(self):
        if self.root.data is None:
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

        print()

    def isHeap(self):
        if self.root.data is None:
            return
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result = self.check_value(current_node)
            if result is False:
                return False
            elif result is True:
                queue.append(current_node.left)
                if current_node.right is not None:
                    queue.append(current_node.right)
                else:
                    break
            elif result is None:
                break

        while len(queue) > 0:
            current_node = queue.pop()
            result = self.check_leaf(current_node)
            if result is True:
                continue
            else:
                return False

        return True

    def mystery(self, x):
        if x == None:
            return 0
        else:
            return max(self.mystery(x.left), self.mystery(x.right))

    def m2(self):
        return self.mystery(self.root)

tree = BST()
import time
import random
start = time.time()
for i in range(10000):
    tree.insert(random.randint(0, 1000))
print(tree.inorder())
end = time.time()

print(end - start)


# tree2 = BT(1)
# tree2.insert(tree2.root, 2, side='L')
# tree2.insert(tree2.root, 3, side='R')
# tree2.insert(tree2.root.left, 4, side='L')
# tree2.insert(tree2.root.left, 5, side='R')
# tree2.insert(tree2.root.right, 6, side='L')
# tree2.insert(tree2.root.right, 7, side='R')
# tree2.insert(tree2.root.left.left, 8, side='L')
# tree2.insert(tree2.root.left.left, 9, side='R')
# tree2.insert(tree2.root.left.right, 10, side='L')
# tree2.insert(tree2.root.left.right, 11, side='R')
# print(tree2.m2())