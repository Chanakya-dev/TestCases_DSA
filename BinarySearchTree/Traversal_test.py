import unittest
from io import StringIO
import sys
from Traversal import Node, inorder  # Adjust the import path as needed

class TestInorderTraversal(unittest.TestCase):
    def setUp(self):
        # Backup the standard output
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Restore standard output
        self.held_output.close()
        sys.stdout = sys.__stdout__

    def capture_inorder_output(self, root):
        """Helper function to capture the inorder output as a string."""
        inorder(root)
        return self.held_output.getvalue().strip()

    def test_empty_tree(self):
        # Test inorder traversal on an empty tree
        root = None
        result = self.capture_inorder_output(root)
        self.assertEqual(result, "")  # Expecting no output

    def test_single_node_tree(self):
        # Test inorder traversal on a single-node tree
        root = Node(100)
        result = self.capture_inorder_output(root)
        self.assertEqual(result, "100")

    def test_left_skewed_tree(self):
        # Test inorder traversal on a left-skewed tree
        root = Node(100)
        root.left = Node(50)
        root.left.left = Node(25)
        result = self.capture_inorder_output(root)
        self.assertEqual(result, "25 50 100")

    def test_right_skewed_tree(self):
        # Test inorder traversal on a right-skewed tree
        root = Node(100)
        root.right = Node(150)
        root.right.right = Node(200)
        result = self.capture_inorder_output(root)
        self.assertEqual(result, "100 150 200")

    def test_balanced_tree(self):
        # Test inorder traversal on a balanced tree
        root = Node(100)
        root.left = Node(50)
        root.right = Node(150)
        root.left.left = Node(25)
        root.left.right = Node(75)
        root.right.left = Node(125)
        root.right.right = Node(200)
        result = self.capture_inorder_output(root)
        self.assertEqual(result, "25 50 75 100 125 150 200")

    def test_unbalanced_tree(self):
        # Test inorder traversal on an unbalanced tree
        root = Node(100)
        root.left = Node(50)
        root.left.left = Node(25)
        root.right = Node(150)
        root.right.right = Node(200)
        root.right.right.right = Node(300)
        result = self.capture_inorder_output(root)
        self.assertEqual(result, "25 50 100 150 200 300")

if __name__ == "__main__":
    unittest.main()
