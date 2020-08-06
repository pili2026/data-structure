class Node:
    def __init__(self, x):
        self.value = x
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def print_list(self):
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head

            # The node traversal (traversal or search), from the head node to the last node
            while current is not None:
                print(current.value, end=" ")
                current = current.next
            print()

    # Insert data at the top of the list
    def push_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    # Remove the first data in the list
    def pop_front(self):
        temp_node = self.head
        if temp_node is None:
            print("List is empty")
        else:
            self.head = temp_node.next
            temp_node = None
        self.size -= 1

    # Insert data at the end of the list
    def push_back(self, data):
        if self.head is None:
            self.push_front(data)
        else:
            temp_node = self.head
            while temp_node.next is not None:
                temp_node = temp_node.next
            temp_node.next = Node(data)
            self.size += 1

    # Remove the last data in the list
    def pop_back(self):
        temp_node = self.head
        if temp_node is None:
            print("List is empty")
        else:
            while temp_node.next.next is not None:
                temp_node = temp_node.next
            temp_node.next = None
        self.size -= 1

    # Delete the data in the list
    def delete_data(self, data):
        previous = None
        current = self.head

        # If current is null or current data is what we want to delete, stop traversal
        while current is not None and current.value != data:
            previous = current
            current = current.next

        # current is null means the list is empty or there is no data in the list we want to delete
        if current is None:
            print("There is no " + str(data) + " in list")

        # If the data we want to delete is the first node
        elif current == self.head:
            self.head = current.next
            current = None
            self.size -= 1

        # The data you want to delete is not the first node
        else:
            previous.next = current.next
            current = 0
            self.size -= 1

    # Clear all data in the list
    def clear(self):
        while self.head is not None:
            current = self.head
            self.head = current.next
            current = 0
        self.size = 0

    # Invert the entire list
    def reverse(self):
        #  If the list is empty or only 1 node, then no action is required
        if self.head is not None and self.head.next is not None:
            previous = None
            current = self.head

            # From the first Null node traversal to the last node
            while current:
                next_node = current.next  # Use variables to record the original next node
                print("next_node:", next_node.value if next_node else None)
                current.next = previous  # Point the node in reverse
                print("current.next:", current.next.value if current.next else None)
                previous = current
                print("previous:", previous.value if previous else None)
                current = next_node
                print("current:", current.value if current else None)
            self.head = previous

    # Return the number of list data
    def get_size(self):
        return self.size

    # Returns whether the list is empty
    def is_empty(self):  # Returns whether the list is empty
        return self.head is None


def main():
    linked_list = SinglyLinkedList()
    linked_list.print_list()
    print(linked_list.is_empty())
    print(linked_list.get_size())
    linked_list.delete_data(4)
    linked_list.push_back(1)
    print(linked_list.get_size())
    linked_list.push_back(3)
    linked_list.push_front(5)
    linked_list.push_front(7)
    linked_list.print_list()
    print(linked_list.is_empty())
    print(linked_list.get_size())
    linked_list.pop_back()
    linked_list.push_back(9)
    linked_list.delete_data(5)
    linked_list.print_list()
    linked_list.push_front(11)
    linked_list.push_front(16)
    linked_list.push_back(13)
    linked_list.print_list()
    linked_list.pop_front()
    linked_list.push_back(15)
    linked_list.delete_data(1)
    linked_list.print_list()
    linked_list.reverse()
    linked_list.print_list()
    print(linked_list.is_empty())
    print(linked_list.get_size())
    linked_list.clear()
    linked_list.print_list()


if __name__ == "__main__":
    main()

