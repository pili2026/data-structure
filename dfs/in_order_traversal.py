class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Traversal:
    """Left->Root->Right"""
    def in_order_traversal_recursive(self, root: Node):
        if root is None:
            return []
        result = []

        if root:
            result = result + self.in_order_traversal_recursive(root.left)
            result.append(root.val)
            result = result + self.in_order_traversal_recursive(root.right)

        return result

    def in_order_traversal_iteration(self, root: Node):
        if root is None:
            return []
        """stack: Last-In-First-Out"""
        result = []
        stack = []
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result


if __name__ == '__main__':
    binary_tree = Traversal()
    node = Node(1)
    # node.left = Node(2)
    node.right = Node(2)
    # node.left.left = Node(4)
    # node.left.right = Node(5)
    node.right.left = Node(3)
    # node.right.right = Node(7)

    '''
    tree:
            1
        2       3
      4   5   6   7
    '''

    print(binary_tree.in_order_traversal_recursive(node))
    print(binary_tree.in_order_traversal_iteration(node))
