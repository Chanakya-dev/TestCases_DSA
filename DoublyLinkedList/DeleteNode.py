class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Function to delete a node in the doubly linked list
    def delete_node(self, key):
        # If the list is empty, print a message
        if not self.head:
            print("The list is empty. Deletion not possible.")
            return self.head

        # Create a pointer to traverse the list
        temp = self.head

        # Case 1: Deleting the head node
        if temp.data == key:
            self.head = temp.next
            if self.head:
                self.head.prev = None
            return self.head

        # Traverse the list to find the node with the given key
        while temp and temp.data != key:
            temp = temp.next

        # Case 2: If the node is not found
        if not temp:
            print("Node not found.")
            return self.head

        # Case 3: Deleting an intermediate node
        # Update the next pointer of the previous node
        if temp.prev:
            temp.prev.next = temp.next

        # Update the previous pointer of the next node
        if temp.next:
            temp.next.prev = temp.prev

        # Case 4: Deleting the last node
        # If it's the last node, update the previous node's next to None
        if not temp.next:
            if temp.prev:
                temp.prev.next = None

        return self.head

    # Function to insert a node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    # Function to print the list
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <=> ")
            temp = temp.next
        print("None")


# Example usage:
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)

print("Original list:")
dll.print_list()

# Deleting the head node
dll.delete_node(10)
print("After deleting 10 (head node):")
dll.print_list()

# Deleting an intermediate node
dll.delete_node(20)
print("After deleting 20 (intermediate node):")
dll.print_list()

# Deleting the last node
dll.delete_node(30)
print("After deleting 30 (last node):")
dll.print_list()

# Trying to delete a non-existent node
dll.delete_node(40)
