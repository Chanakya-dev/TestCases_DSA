class Node:
    def __init__(self, data):
        """Initialize a node with data and a next pointer."""
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        """Initialize an empty circular linked list."""
        self.head = None

    def add_last(self, value):
        """
        Add a new node with the given value to the end of the circular linked list.
        """
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
            # Traverse to the last node (the one pointing to the head)
            while last_node.next != self.head:
                last_node = last_node.next

            # Step 3: Insert the new node after the last node
            last_node.next = new_node

            # Step 4: Update the new node to point to the head
            new_node.next = self.head


# Utility function to print the circular linked list
def print_circular_list(cll):
    """
    Print the circular linked list in a human-readable format.
    """
    if cll.head is None:
        print("The list is empty.")
        return

    current = cll.head
    while True:
        print(current.data, end=" -> ")
        current = current.next
        if current == cll.head:
            break
    print(f"(back to {cll.head.data})")


# Example usage:
if __name__ == "__main__":
    cll = CircularLinkedList()

    # Insert nodes into the circular linked list
    cll.add_last(10)
    cll.add_last(20)
    cll.add_last(30)
    cll.add_last(40)

    # Print the circular linked list after insertions
    print_circular_list(cll)
