import unittest
from DeleteNode import delete_node,Node
class TestDeleteNode(unittest.TestCase):
    def setUp(self):
        # Create a tree for testing
        self.root = Node(100)
        self.root.left = Node(50)
        self.root.right = Node(200)
        self.root.left.left = Node(10)
        self.root.left.right = Node(75)
        self.root.right.left = Node(150)
        self.root.right.right = Node(250)

    def test_delete_leaf_node(self):
        # Delete a leaf node (10)
        self.root = delete_node(self.root, 10)
        # Verify that the node is deleted
        self.assertIsNone(self.root.left.left)

    def test_delete_node_with_one_child(self):
        # Delete a node with one child (150)
        self.root = delete_node(self.root, 150)
        # Verify that 150 is replaced correctly
        self.assertIsNone(self.root.right.left)

    def test_delete_node_with_two_children(self):
        # Delete a node with two children (200)
        self.root = delete_node(self.root, 200)
        # Verify that 200 is replaced with its inorder successor (250)
        self.assertEqual(self.root.right.key, 250)
        # Verify that 250 is removed from its original position
        self.assertIsNone(self.root.right.right)

    def test_delete_root_node(self):
        # Delete the root node (100)
        self.root = delete_node(self.root, 100)
        # Verify the new root is the inorder successor (150)
        self.assertEqual(self.root.key, 150)

    def test_delete_nonexistent_node(self):
        # Attempt to delete a node that doesn't exist (300)
        initial_root = self.root
        self.root = delete_node(self.root, 300)
        # Verify the tree remains unchanged
        self.assertEqual(self.root, initial_root)

    def test_delete_from_empty_tree(self):
        # Delete from an empty tree
        empty_tree = None
        empty_tree = delete_node(empty_tree, 100)
        # Verify the result is still None
        self.assertIsNone(empty_tree)

if __name__ == "__main__":
    unittest.main()
