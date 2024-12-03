class Node:
    def __init__(self, data):
        self.data = data  # Stores the data of the node
        self.next = None  # Points to the next node
        self.prev = None  # Points to the previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list

    # Function to search for a node in the doubly linked list
    def search_node(self, key):
        temp = self.head  # 1. Start by creating a pointer at the head node to traverse the list

        # 2. Iterate through the list until the pointer reaches the end (None)
        while temp:
            # 3. Check if the current node contains the key
            if temp.data == key:
                # 4. If the key matches the current node's data, return True (key found)
                return True

            # 5. If the key doesn't match, move the pointer to the next node
            temp = temp.next

        # 6. If we exit the loop, the key was not found, so return False
        return False

# Example usage
dll = DoublyLinkedList()

# Adding nodes to the doubly linked list
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

dll.head = node1
node1.next = node2
node2.prev = node1
node2.next = node3
node3.prev = node2

# Searching for nodes in the doubly linked list
print(dll.search_node(30))  # Output: True (30 is found)
print(dll.search_node(100))  # Output: False (100 is not found)
