# Node class to represent each node in the doubly linked list
class Node:
    def __init__(self, val):
        self.val = val  # Node value
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

# DoublyLinkedList class to represent the doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the doubly linked list with an empty head

    def add_last(self, val):
        # Create a new node with the given value
        new_node = Node(val)

        # Case 1: If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node  # The new node becomes the head
            return

        # Case 2: If the list is not empty, find the last node
        last = self.head
        while last.next is not None:
            last = last.next  # Move to the next node

        # Insert the new node after the last node
        last.next = new_node  # Last node's next points to the new node
        new_node.prev = last  # New node's prev points to the last node

    # Method to print the doubly linked list (for demonstration purposes)
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" <-> " if current.next else "")
            current = current.next
        print()

# Demo: Insert nodes at the end of the doubly linked list
dll = DoublyLinkedList()  # Create an empty doubly linked list

# Insert the first node with value 10
dll.add_last(10)  
# Insert the second node with value 20
dll.add_last(20)  
# Insert the third node with value 30
dll.add_last(30)  
# Insert the fourth node with value 100
dll.add_last(100)  

# Print the final list
dll.print_list()  # Expected output: 10 <-> 20 <-> 30 <-> 100
