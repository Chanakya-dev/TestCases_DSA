class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data for the node
        self.next = None  # Initialize the next pointer

class CircularLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    def delete_node(self, key):
        # Step 1: Check if the list is empty
        if not self.head:
            print("List is empty. Deletion cannot be performed.")
            return

        # Step 2: Check if the node to be deleted is the head
        if self.head.data == key:
            if self.head.next == self.head:  # Only one node in the list
                self.head = None  # Delete the head node
            else:  # More than one node in the list
                last_node = self.head
                while last_node.next != self.head:  # Traverse to the last node
                    last_node = last_node.next
                # Point the last node to the second node and make it the new head
                last_node.next = self.head.next
                self.head = self.head.next
            return

        # Step 3: Delete a node other than the head
        current = self.head
        while current.next != self.head:  # Traverse until we reach the head again
            if current.next.data == key:  # Found the node to delete
                current.next = current.next.next  # Bypass the node to delete it
                return
            current = current.next

        # If the key is not found
        print(f"Node with data {key} not found.")

# Example usage
cll = CircularLinkedList()

# Create nodes and link them
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

cll.head = node1
node1.next = node2
node2.next = node3
node3.next = node1  # Making it circular

# Delete nodes
cll.delete_node(10)  # Deleting the head node
cll.delete_node(30)  # Deleting a non-head node
cll.delete_node(40)  # Trying to delete a non-existent node
