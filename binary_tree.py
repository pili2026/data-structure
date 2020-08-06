class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_height(self):
        if self.left and self.right:
            return 1 + max(self.left.get_height(), self.right.get_height())
        elif self.left:
            return 1 + self.left.get_height()
        elif self.right:
            return 1 + self.right.get_height()
        else:
            return 1


class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def get_height(self):
        if self.root:
            return self.root.get_height()
        else:
            return -1

    def print_tree(self, tree, traversal_type):
        if traversal_type == "preorder":
            return self.pre_order_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.in_order_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.post_order_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.level_order_print(tree.root)
        elif traversal_type == "reverse_levelorder":
            return self.reverse_levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False

    def pre_order_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.pre_order_print(start.left, traversal)
            traversal = self.pre_order_print(start.right, traversal)
        return traversal

    def in_order_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.in_order_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.in_order_print(start.right, traversal)
        return traversal

    def post_order_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.post_order_print(start.left, traversal)
            traversal = self.post_order_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def level_order_print(self, start):
        if start is None:
            return

        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return

        queue = Queue()
        stack = Stack()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            node = queue.dequeue()
            stack.push(node)

            if node.right:
                queue.enqueue(node.right)
            if node.left:
                queue.enqueue(node.left)

        while len(stack) > 0:
            node = stack.pop()
            traversal += str(node.value) + "-"

        return traversal


def binary_tree_traversal(traversal: str):
    #               1
    #           /       \
    #          2          3
    #         /  \      /   \
    #        4    5     6   7
    # Set up tree:
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)

    print(tree.print_tree(tree, traversal))
    print("tree height:", tree.get_height())


if __name__ == '__main__':
    # binary_tree_traversal("preorder")
    # binary_tree_traversal("inorder")
    # binary_tree_traversal("postorder")
    binary_tree_traversal("levelorder")
    # binary_tree_traversal("reverse_levelorder")
