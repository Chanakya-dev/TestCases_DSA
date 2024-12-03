class Node:
    def __init__(self, value):
        self.key = value  # Node value
        self.left = None  # Left child
        self.right = None  # Right child

def insert(root, value):
    # If the tree is empty, create a new node and return it as root
    if root is None:
        return Node(value)
    
    # If the value is smaller than the root, insert in the left subtree
    if value < root.key:
        root.left = insert(root.left, value)
    
    # If the value is greater than the root, insert in the right subtree
    elif value > root.key:
        root.right = insert(root.right, value)
    
    # Return the root node after insertion
    return root

def search(root, key):
    # If the tree is empty, return False (key not found)
    if root is None:
        return False
    
    # If the key matches the root node's key, return True (key found)
    if root.key == key:
        return True
    
    # If the key is smaller than the root, search in the left subtree
    if key < root.key:
        return search(root.left, key)
    
    # If the key is larger than the root, search in the right subtree
    return search(root.right, key)

# Example Usage:
root = None

# Inserting nodes into the BST
root = insert(root, 100)
root = insert(root, 50)
root = insert(root, 150)
root = insert(root, 125)

# Searching for nodes in the BST
print(search(root, 60))  # Output: False (not found)
print(search(root, 150)) # Output: True (found)
print(search(root, 500)) # Output: False (not found)
