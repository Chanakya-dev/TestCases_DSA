class Node:
    def __init__(self, data):
        self.data = data  # Initialize node data
        self.next = None  # Initialize the next pointer


class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def add_first(self, value):
        """Add a new node with the given value at the beginning of the circular linked list."""
        # Step 1: Create a new node with the given value
        new_node = Node(value)

        # Step 2: Check if the list is empty
        if not self.head:
            # Case 1: If the list is empty
            new_node.next = new_node  # Point the new node to itself
            self.head = new_node  # Make the new node the head
        else:
            # Case 2: If the list is not empty
            last_node = self.head
            # Find the last node (the one pointing to the head)
            while last_node.next != self.head:
                last_node = last_node.next
            # Insert the new node after the last node
            last_node.next = new_node
            # Point the new node to the current head
            new_node.next = self.head
            # Make the new node the head
            self.head = new_node

    def display(self):
        """Display the circular linked list."""
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(Back to head)")
