class Product_Node:
    def __init__(self, p_code: str, p_name: str, quantity: int, sale: int, price: float):
        self.p_code = p_code
        self.p_name = p_name
        self.quantity = quantity
        self.sale = sale
        self.price = price
        self.left = self.right = None


class Customer_Node:
    def __init__(self, c_code: str, c_name: str, phone: str):
        self.c_code = c_code
        self.c_name = c_name
        self.phone = phone
        self.next = None


class Ordering_Node:

    def __init__(self, p_code: str, c_code: str, quantity: int):
        self.p_code = p_code
        self.c_code = c_code
        self.quantity = quantity
        self.next = None


class Product_BST:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def load_file(self, file_name='product_info.txt'):
        """Load data from file into product tree"""
        with open(file_name, 'r') as file:
            file = file.readlines()[1:]
            file = [ele.split('|') for ele in file]
            for p_code, p_name, quantity, sale, price in file:
                self.insert(p_code, p_name, int(quantity), float(price), int(sale))

    def insert(self, p_code, p_name, quantity, price, sale=0):
        if self.isEmpty():
            self.root = Product_Node(p_code, p_name, quantity, sale, price)
        else:
            curr_node = self.root
            while True:
                if p_code == curr_node.p_code:
                    p_code = input('P_code existed, please enter other p_code:')
                    continue
                elif p_code < curr_node.p_code:
                    if not curr_node.left:
                        curr_node.left = Product_Node(p_code, p_name, quantity, sale, price)
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if not curr_node.right:
                        curr_node.right = Product_Node(p_code, p_name, quantity, sale, price)
                        break
                    else:
                        curr_node = curr_node.right

    def visit(self, node):
        print(" {:<10} | {:<15} | {:<10} | {:<10} | {:<6} ".format(node.p_code, node.p_name, node.quantity, node.sale,
                                                                  node.price))

    def inorder_recur(self, node):
        if node:
            if node.left:
                self.inorder_recur(node.left)
            self.visit(node)
            if node.right:
                self.inorder_recur(node.right)

    def inorder(self):
        if self.isEmpty():
            print('No product found.')
        else:
            header = " {:<10} | {:<15} | {:<10} | {:<10} | {:<6} ".format("P_code", "P_name", "Quantity", "Sale", "Price")
            print(header)
            print("-" * len(header))
            self.inorder_recur(self.root)

    def breadth(self):
        if self.isEmpty():
            return
        header = " {:<10} | {:<15} | {:<10} | {:<10} | {:<6} ".format("P_code", "P_name", "Quantity", "Sale", "Price")
        print(header)
        print("-" * len(header))
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            self.visit(current_node)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

    def save(self, file_name='product_info.txt'):
        with open(file_name, 'w') as file:
            file.write("Pcode|Pname|Quantity|Sale|Price\n")

            if self.isEmpty():
                return

            queue = []

            queue.append(self.root)
            while len(queue) > 0:
                current = queue.pop(0)
                file.write(f"{current.p_code}|{current.p_name}|{current.quantity}|{current.sale}|{current.price}\n")
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

    def breadth_and_delete(self):
        if self.isEmpty():
            return

        queue = []
        delete_list = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node.quantity == 0:
                delete_list.append(current_node.p_code)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        for p_code in delete_list:
            self.dele(p_code)

    def search(self, x: str):
        if self.isEmpty():
            return None
        else:
            curr_node = self.root
            while curr_node:
                if x == curr_node.p_code:
                    return curr_node
                elif x < curr_node.p_code:
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right
            return False

    def dele(self, p_code):
        if self.isEmpty():
            return None

        parent_node = None
        node_to_delete = self.root

        # Find the node to delete and its parent
        while node_to_delete is not None and node_to_delete.data != p_code:
            parent_node = node_to_delete
            if p_code < node_to_delete.data:
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
            node_to_delete.p_code = temp_val

    def min_for_small_tree(self, node):
        if self.isEmpty():
            return None
        else:
            curr_node = node
            while curr_node.left:
                curr_node = curr_node.left

            return curr_node.p_code

    def preorder_recur(self, node, nodes_list: list):
        if node:
            self.preorder_recur(node.left, nodes_list)
            nodes_list.append(node)
            self.preorder_recur(node.right, nodes_list)

    def store_nodes(self, nodes_list: list):
        self.preorder_recur(self.root, nodes_list)

    # Recursive function to construct binary tree
    def build_tree(self, nodes: list, start, end):

        # base case
        if start > end:
            return None

        # Get the middle element and make it root
        mid = (start + end) // 2
        node = nodes[mid]

        # Using index in Inorder traversal, construct
        # left and right subtress
        node.left = self.build_tree(nodes, start, mid - 1)
        node.right = self.build_tree(nodes, mid + 1, end)
        return node

    # This functions converts an unbalanced BST to
    # a balanced BST
    def simply_balance(self):

        # Store nodes of given BST in sorted order
        nodes_list = []
        self.store_nodes(nodes_list)

        # Constructs BST from nodes[]
        n = len(nodes_list)
        return self.build_tree(nodes_list, 0, n - 1)

    def count(self):
        if self.isEmpty():
            return 0
        num_product = 0
        num_quantity = 0
        queue = []
        queue.append(self.root)
        while len(queue) > 0:
            current_node = queue.pop(0)
            num_product += 1
            num_quantity += current_node.quantity
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return num_product, num_quantity

    def change(self, node, name, quantity, price):
        node.p_name = name
        node.quantity = quantity
        node.price = price

class Customer_List:
    def __init__(self):
        self.head = None

    def load_file(self, file_name='customers_info.txt'):
        with open(file_name, 'r') as file:
            file = file.readlines()[1:]
            file = [ele.split('|') for ele in file]
            for c_code, c_name, phone in file:
                self.load_element(c_code, c_name, phone)

    def load_element(self, c_code, c_name, phone):
        new_node = Customer_Node(c_code, c_name, phone)
        # Thêm sách
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        """
        Display information about customers.
        """
        current = self.head
        if not current:
            print("Empty.")
            return
        header = " {:<5} | {:<10} | {:<15} ".format("C_code", "C_name", "Phone")
        print(header)
        print("-"*len(header))
        while current:
            print(" {:<5} | {:<10} | {:<15} ".format(current.c_code, current.c_name, current.phone))
            current = current.next

    def save_file(self, file_name='customers_info.txt'):
        """Save information about customer in to file"""
        with open(file_name, 'w') as file:
            file.write("Ccode|Cname|Phone\n")
            current = self.head
            while current:
                file.write(f"{current.c_code}|{current.c_name}|{current.phone}")
                current=current.next
        return file_name

    def search(self, c_code):
        if not self.head:
            return 'Empty'
        else:
            curr_node = self.head
            while curr_node:
                if c_code == curr_node.p_code:
                    return curr_node
                else:
                    curr_node = curr_node.next
            return 'Not found'

    def delete(self, c_code):
        current = self.head
        previous = None
        while current:
            if current.c_code == c_code:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                return True
            previous = current
            current = current.next
        return False

class Order_List:
    def __init__(self):
        self.head = None

    def load_file(self, file_name='order_info.txt'):
        with open(file_name, 'r') as file:
            file = file.readlines()[1:]
            file = [ele.split('|') for ele in file]
            for p_code, c_code, quantity in file:
                self.load_element(p_code, c_code, quantity)

    def load_element(self, p_code, c_code, quantity):
        new_node = Ordering_Node(p_code, c_code, quantity)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        """
        Display information about customers.
        """
        self.sort()
        current = self.head
        if not current:
            print("Empty.")
            return
        header = " {:<5} | {:<10} | {:<15} ".format("P_code", "C_code", "Quantity")
        print(header)
        print("-"*len(header))
        while current:
            print(" {:<5} | {:<10} | {:<15} ".format(current.p_code, current.c_code, current.quantity))
            current = current.next

    def save_file(self, file_name='order_info.txt'):
        """Save information about customer in to file"""
        with open(file_name, 'w') as file:
            file.write("Pcode|Ccode|Quantity\n")
            current = self.head
            while current:
                file.write(f"{current.p_code}|{current.c_code}|{current.quantity}")
                current=current.next
        return file_name

    def search(self, c_code):
        if not self.head:
            return 'Empty'
        else:
            curr_node = self.head
            while curr_node:
                if c_code == curr_node.p_code:
                    return curr_node
                else:
                    curr_node = curr_node.next
            return 'Not found'

    def insert(self, p_code, c_code, quantity):
        new_node = Ordering_Node(p_code, c_code, quantity)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def sort(self):
        store_dict = {}
        curr_node = self.head
        while curr_node:
            store_dict[curr_node.p_code + curr_node.c_code] = curr_node
            curr_node = curr_node.next

        self.head = None
        # sort_list = list(store_dict.keys())
        # sort_list.sort()
        # store_dict = {i: store_dict[i] for i in sort_list}

        for key in sorted(store_dict):
            node = store_dict[key]
            self.insert(node.p_code, node.c_code, node.quantity)

def menu():
    Products = Product_BST()
    Products.load_file()

    Customers = Customer_List()
    Customers.load_file()

    Order = Order_List()
    Order.load_file()

    while True:
        print("\nSales and Inventory Management System")
        print("1. Register product arrival")
        print("2. Query inventory data")
        print("3. Exit\n")

        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            print('---------------------------------')
            print('Register product arrival')

            while True:

                print("\n1. Edit product details")
                print("2. Add stock to the product")
                print("3. Remove product that are out of stock")
                print("4. Exit\n")

                choice_1 = input("Enter your choice (1-4): ")

                if choice_1 == '1':
                    input_p_code = input('Enter your product code: ')
                    result = Products.search(input_p_code)
                    if result == None:
                        print('Empty tree.')
                    elif result == False:
                        print('\nNot found this product code.\n')
                        continue
                    else:
                        new_name = input("Enter new product name : ")
                        new_quantity = int(input("Enter quantity : "))
                        new_price = float(input("Enter new price : "))

                        Products.change(result, new_name, new_quantity, new_price)
                        print('Finish!')

                        continue

                elif choice_1 == '2':
                    print('---------------------------------')
                    print('Add stock to the product')

                    p_code = input("Enter new product code : ")
                    p_name = input("Enter new product name : ")
                    quantity = int(input("Enter quantity         : "))
                    price = float(input("Enter price           : "))

                    Products.insert(p_code, p_name, quantity, price)
                    print('Finish!')

                    continue

                elif choice_1 == '3':
                    Products.breadth_and_delete()
                    print('Finish!')

                    continue

                elif choice_1 == '4':
                    break

                else:
                    print("\nInvalid choice. Please enter a number between 1 and 4.")

        elif choice == '2':


            while True:
                print('\n---------------------------------')
                print('Query inventory data\n')
                print("1. View product table")
                print("2. View customer table")
                print("3. View order table")
                print("4. Exit")

                choice_2 = input("\nEnter your choice (1-4): ")
                print()

                if choice_2 == '1':
                    Products.inorder()
                    continue
                elif choice_2 == '2':
                    Customers.display()
                    continue
                elif choice_2 == '3':
                    Order.display()
                    continue
                elif choice_2 == '4':
                    break
                else:
                    print("\nInvalid choice. Please enter a number between 1 and 4.")

        elif choice == '3':
            file_name = 'product_info.txt'
            Products.save(file_name)
            Customers.save_file()
            Order.save_file()
            print(f"\nInformation stored in the file {file_name}.")
            print("\nThank you for using the Sales and Inventory Management System.")

            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 3.")

def main():
    menu()

if __name__ == "__main__":
    main()
