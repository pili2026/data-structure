class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Traversal:
    """pre-order : Root->Left->Right"""
    def pre_order_traversal_recursive(self, root):
        if root is None:
            return []
        result = []

        if root:
            result.append(root.val)
            result = result + self.pre_order_traversal_recursive(root.left)
            result = result + self.pre_order_traversal_recursive(root.right)

        return result

    def pre_order_traversal_iteration(self, root: Node):
        if root is None:
            return []

        result = []
        """
        dfs use stack.
        stack: Last-In-First-Out
        """
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                result.append(node.val)
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        return result


if __name__ == '__main__':
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

    print(binary_tree.pre_order_traversal_recursive(tree_node))
    print(binary_tree.pre_order_traversal_iteration(tree_node))
