class Node:
    def __init__(self, data):
        # Each node has data and a pointer to the next node
        self.data = data
        self.next = None  # Initialize the next pointer to None

class CircularLinkedList:
    def __init__(self):
        # The circular linked list starts with an empty head
        self.head = None

    def search(self, key):
        # Step 1: Check if the list is empty
        if not self.head:
            return False  # No nodes to search in

        # Step 2: Start traversing from the head node
        temp = self.head

        while True:
            # Step 3: Compare the key with the current node's data
            if temp.data == key:
                return True  # Key found

            # Step 4: Move to the next node
            temp = temp.next

            # Step 5: Check if we've returned to the head node
            if temp == self.head:
                break  # Stop the traversal when the list is fully traversed

        # Step 6: If no match is found, return False
        return False

# Example Usage
# Creating nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Linking nodes to form a circular linked list
cll = CircularLinkedList()
cll.head = node1
node1.next = node2
node2.next = node3
node3.next = node1  # Points back to the head node

# Testing the search function
print(cll.search(30))  # Output: True
print(cll.search(100))  # Output: False
