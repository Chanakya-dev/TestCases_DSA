class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        # Step 1: Create a new node
        new_node = Node(data)

        # Step 2: Set the new node's next to the current head
        new_node.next = self.head

        # Step 3: Update the head to the new node
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert_at_beginning(10)  # Insert 10 at the beginning
linked_list.insert_at_beginning(20)  # Insert 20 at the beginning
linked_list.insert_at_beginning(30)  # Insert 30 at the beginning

linked_list.display()  # Output: 30 -> 20 -> 10 -> None
