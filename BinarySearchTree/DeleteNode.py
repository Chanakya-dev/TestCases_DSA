class Node:
    def __init__(self, key):
        self.key = key  # Node value
        self.left = None  # Left child
        self.right = None  # Right child

def find_min(node):
    # Function to find the minimum value in a subtree (leftmost node)
    while node.left is not None:
        node = node.left
    return node

def delete_node(root, key):
    # Function to delete a node with the specified key while maintaining BST properties
    if root is None:
        return root  # If the tree is empty or key is not found, return None

    # Step 1: Find the node to delete by comparing the key with the current node's key
    if key < root.key:
        root.left = delete_node(root.left, key)  # Search in the left subtree
    elif key > root.key:
        root.right = delete_node(root.right, key)  # Search in the right subtree
    else:
        # Case 1: Node has no children (leaf node)
        if root.left is None and root.right is None:
            return None  # Simply delete the node by returning None

        # Case 2: Node has only one child
        if root.left is None:
            return root.right  # Return the right child to replace the node
        elif root.right is None:
            return root.left  # Return the left child to replace the node

        # Case 3: Node has two children
        # Find the inorder successor (the smallest node in the right subtree)
        temp = find_min(root.right)
        root.key = temp.key  # Replace the node's key with the inorder successor's key
        # Delete the inorder successor from the right subtree
        root.right = delete_node(root.right, temp.key)

    return root  # Return the updated root of the subtree

# Example Usage
root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(10)
root.left.right = Node(75)
root.right.left = Node(150)
root.right.right = Node(250)

# Deleting nodes
root = delete_node(root, 10)  # Delete leaf node 10
root = delete_node(root, 150)  # Delete node with one child (150)
root = delete_node(root, 200)  # Delete node with two children (200)

# Print the updated BST (This part can be extended with a print function to visualize the tree)
