class Node:
    """Defines a node"""

    def __init__(self, data, next_node=None):
        """Initializes the node with instance variables"""
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.data = data
        self.next_node = next_node

    # Rest of the code remains the same

class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initializes the singly linked list"""
        self.head = None

    # Rest of the code remains the same
