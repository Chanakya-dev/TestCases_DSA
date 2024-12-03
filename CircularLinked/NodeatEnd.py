class Node:
    def __init__(self, data):
        self.data = data  # Initialize node data
        self.next = None  # Initialize the next pointer

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def add_last(self, value):
        # Step 1: Create a new node with the given value
        new_node = Node(value)

        # Step 2: Check if the list is empty
        if not self.head:
            # If the list is empty, the new node points to itself and becomes the head
            new_node.next = new_node  # Point the new node to itself
            self.head = new_node  # Make the new node the head
        else:
            # If the list is not empty, traverse to the last node
            last_node = self.head
            while last_node.next != self.head:
                last_node = last_node.next  # Move to the next node

            # Step 3: Insert the new node after the last node
            last_node.next = new_node  # Set the last node's next to the new node

            # Step 4: Update the new node to point to the head
            new_node.next = self.head  # Point the new node to the current head

# Example usage:
cll = CircularLinkedList()

# Insert the first node (10)
cll.add_last(10)  # The new node points to itself and becomes the head

# Insert the second node (20)
cll.add_last(20)  # Traverse to last node, then insert after it

# Insert the third node (30)
cll.add_last(30)  # Traverse to last node, then insert after it

# Insert the fourth node (40)
cll.add_last(40)  # Traverse to last node, then insert after it

# Printing the circular linked list
# This is a utility function to print the circular linked list
def print_circular_list(cll):
    if cll.head is None:
        print("The list is empty.")
        return

    current = cll.head
    while True:
        print(current.data, end=" → ")
        current = current.next
        if current == cll.head:
            break
    print("back to", cll.head.data)

# Print the circular linked list after insertions
print_circular_list(cll)
