# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data        # Stores the data of the node.
        self.next = None        # Points to the next node.

# Define the LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None        # Points to the head of the linked list.

    def search(self, key):
        temp = self.head                         # Start traversing from the head node.
        while temp is not None:                  # Traverse the list until the end of the linked list.
            if temp.data == key:                 # Compare each node's data with the key.
                return True                      # Return true if the key is found in the linked list.
            temp = temp.next                     # Move to the next node if the key is not found.
        return False                             # Return false if the key is not found in the linked list.

# Example usage:
if __name__ == "__main__":
    # Create a linked list and add some nodes
    linked_list = LinkedList()
    linked_list.head = Node(10)
    second = Node(20)
    third = Node(30)
    fourth = Node(40)

    # Link the nodes
    linked_list.head.next = second
    second.next = third
    third.next = fourth

    # Search for a key in the linked list
    key = 30
    result = linked_list.search(key)

    if result:
        print(f"Key {key} found in the linked list.")
    else:
        print(f"Key {key} not found in the linked list.")
