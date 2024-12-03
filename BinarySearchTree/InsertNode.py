class Node:
    def __init__(self, value):
        self.key = value  # The value of the node
        self.left = None  # Left child (initially None)
        self.right = None  # Right child (initially None)

def insert(root, value):
    # If the tree is empty, create a new node and return it
    if root is None:
        return Node(value)

    # If the value to be inserted is less than the root, go to the left subtree
    if value < root.key:
        root.left = insert(root.left, value)
    # If the value to be inserted is greater than the root, go to the right subtree
    elif value > root.key:
        root.right = insert(root.right, value)

    # Return the root after insertion is completed
    return root

# Helper function to print the tree structure for visualization
def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            if root.left:
                print_tree(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Main code to test the insertion
if __name__ == "__main__":
    root = None  # Start with an empty tree

    # Insert nodes
    root = insert(root, 100)  # Insert 100
    root = insert(root, 50)   # Insert 50
    root = insert(root, 150)  # Insert 150
    root = insert(root, 125)  # Insert 125

    # Print the final tree structure
    print_tree(root)
