class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        # Step 1: Create a new node with the given data
        new_node = Node(data)

        # Step 2: If the list is empty, make the new node the head
        if self.head is None:
            self.head = new_node
            return
        
        # Step 3: If the list is not empty, find the last node
        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        # Step 4: Insert the new node after the last node
        last_node.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
linked_list = LinkedList()
linked_list.insert_at_end(10)  # Insert 10 at the end
linked_list.insert_at_end(20)  # Insert 20 at the end
linked_list.insert_at_end(30)  # Insert 30 at the end

linked_list.display()  # Output: 10 -> 20 -> 30 -> None
