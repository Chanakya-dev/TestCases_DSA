import unittest
from Search import insert, search  # Adjust the import path if necessary

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        # Initialize an empty tree before each test
        self.root = None

    def test_insert_into_empty_tree(self):
        # Test inserting into an empty tree
        self.root = insert(self.root, 100)
        self.assertEqual(self.root.key, 100)
        self.assertIsNone(self.root.left)
        self.assertIsNone(self.root.right)

    def test_insert_left_and_right(self):
        # Test inserting nodes to left and right of the root
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 50)
        self.root = insert(self.root, 150)

        self.assertEqual(self.root.key, 100)
        self.assertEqual(self.root.left.key, 50)
        self.assertEqual(self.root.right.key, 150)

    def test_insert_deeper_levels(self):
        # Test inserting at deeper levels in the BST
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 50)
        self.root = insert(self.root, 150)
        self.root = insert(self.root, 125)

        self.assertEqual(self.root.right.left.key, 125)

    def test_search_existing_node(self):
        # Test searching for existing nodes
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 50)
        self.root = insert(self.root, 150)

        self.assertTrue(search(self.root, 100))  # Root node
        self.assertTrue(search(self.root, 50))   # Left child
        self.assertTrue(search(self.root, 150))  # Right child

    def test_search_non_existing_node(self):
        # Test searching for nodes that do not exist
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 50)
        self.root = insert(self.root, 150)

        self.assertFalse(search(self.root, 75))   # Between existing nodes
        self.assertFalse(search(self.root, 200))  # Greater than any node
        self.assertFalse(search(self.root, 25))   # Less than any node

    def test_search_in_empty_tree(self):
        # Test searching in an empty tree
        self.assertFalse(search(self.root, 100))  # No nodes in the tree

if __name__ == "__main__":
    unittest.main()
