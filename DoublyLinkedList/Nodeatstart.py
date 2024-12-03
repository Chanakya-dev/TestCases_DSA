class Node:
    def __init__(self, val):
        self.val = val  # Node value
        self.next = None  # Pointer to the next node
        self.prev = None  # Pointer to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the doubly linked list with an empty head

    def add_first(self, val):
        # Create a new node with the given value
        new_node = Node(val)

        # Case 1: If the list is empty, set the new node as the head
        if self.head is None:
            self.head = new_node  # The new node becomes the head
            return

        # Case 2: If the list is not empty, insert before the current head
        new_node.next = self.head  # New node's next points to the current head
        self.head.prev = new_node  # Current head's prev points to the new node
        self.head = new_node       # Update the new node as the head

    # Method to print the doubly linked list (for demonstration purposes)
    def print_list(self):
        current = self.head
        while current:
            print(current.val, end=" <-> " if current.next else "")
            current = current.next
        print()

# Demo: Insert nodes at the beginning of the doubly linked list
dll = DoublyLinkedList()  # Create an empty doubly linked list

# Insert the first node with value 10
dll.add_first(10)  
# Insert the second node with value 20
dll.add_first(20)  
# Insert the third node with value 30
dll.add_first(30)  

# Print the final list
dll.print_list()  # Expected output: 30 <-> 20 <-> 10
