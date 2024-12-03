class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def inorder(root):
    # If the root is None, the function does nothing and returns
    if root is None:
        return
    
    # Recursively traverse the left subtree
    inorder(root.left)
    
    # Print the key of the current node
    print(root.key, end=" ")
    
    # Recursively traverse the right subtree
    inorder(root.right)

# Constructing the BST
root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(10)
root.left.right = Node(60)
root.right.left = Node(150)
root.right.right = Node(300)

# Calling inorder traversal
inorder(root)
