class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Traversal:
    """Left->Right->Root"""
    def post_order_traversal_recursive(self, root: Node):
        if root is None:
            return []
        result = []
        if root:
            result = result + self.post_order_traversal_recursive(root.left)
            result = result + self.post_order_traversal_recursive(root.right)
            result.append(root.val)
        return result

    def post_order_traversal_iteration(self, root: Node):
        """stack: Last-In-First-Out"""
        if root is None:
            return []
        result = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
        return result[::-1]


if __name__ in "__main__":
    binary_tree = Traversal()
    tree_node = Node(1)
    tree_node.left = Node(2)
    tree_node.right = Node(3)
    tree_node.left.left = Node(4)
    tree_node.left.right = Node(5)
    tree_node.right.left = Node(6)
    tree_node.right.right = Node(7)

    '''
    tree:
            1
        2       3
      4   5   6   7
    '''

    print(binary_tree.post_order_traversal_recursive(tree_node))
    print(binary_tree.post_order_traversal_iteration(tree_node))
