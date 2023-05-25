# Ex1:
def sum(n):
    if n == 1:
        return 1
    else:
        return n + sum(n-1)

# Ex2:
def findmin(list_, length):
    min = list_[length-1]
    if length == 1:
        return list_[0]
    if min <= list_[0]:
        return findmin(list_[1:], length-1)

    if min >= list_[0]:
        return findmin(list_[: length-1], length-1)

# Ex3:
def find_sum(arr, length):
    if length == 0:
        return 0
    else:
        return arr[0] + find_sum(arr[1:], length-1)

# Ex4:
def is_palindrome(arr, length):
    if length > 0 and arr[0] == arr[-1]:
        return is_palindrome(arr[1: -1], length-2)
    elif length > 0 and arr[0] != arr[-1]:
        return 0
    return 1

# Ex5:
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

# Ex6:
def GCD(m, n):
    if n == 0:
        return m
    else:
        return GCD(n, m%n)

# Ex7:
def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)

# Ex8:
def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n - 1)

# Ex9:
def fibo(x):
    if x <= 2:
        return 1
    else:
        return fibo(x - 1) + fibo(x - 2)

# Ex10:
def addReciprocals(n):
    if n == 0:
        return 0
    else:
        return 1/n + addReciprocals(n-1)

# Ex11:
def stirling(n, k):
    if n == 0 and k == 0:
        return 1
    elif n > 0 and k == 0:
        return 0
    elif n >= 0 and k > 0:
        return stirling(n - 1, k - 1) - (n-1) * stirling(n - 1, k)


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Ex12:
def find_size(root):
    if root is None:
        return 0
    else:
        return 1 + find_size(root.left) + find_size(root.right)

# Ex13:
def find_height(root):
    if root is None:
        return -1
    else:
        left_height = find_height(root.left)
        right_height = find_height(root.right)
        return max(left_height, right_height) + 1

