class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Traversal:
    def level_order_traversal_iteration(self,  root: Node):
        """queue -> First-in-First-out"""
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            level_size = len(queue)
            level = []

            for i in range(0, level_size):
                node = queue.pop(0)
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
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

    print(binary_tree.level_order_traversal_iteration(tree_node))
    # print(binary_tree.level_order_traversal_iteration(tree_node))