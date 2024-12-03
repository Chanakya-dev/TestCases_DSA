class Node:
    def __init__(self, data):
        self.data = data  # Initialize node data
        self.next = None  # Initialize the next pointer

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the linked list

    def add_first(self, value):
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

# Example usage:
cll = CircularLinkedList()

# Insert the first node (10)
cll.add_first(10)

# Insert a second node (20)
cll.add_first(20)

# Insert a third node (30)
cll.add_first(30)

# To display the circular linked list (for testing purposes)
def display(cll):
    if not cll.head:
        print("List is empty.")
        return
    temp = cll.head
    while True:
        print(temp.data, end=" → ")
        temp = temp.next
        if temp == cll.head:
            break
    print("(Back to head)")

# Display the circular linked list
display(cll)
