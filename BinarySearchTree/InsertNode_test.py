import unittest
from InsertNode import insert  # Adjust according to your actual module

class TestBinarySearchTree(unittest.TestCase):
    def setUp(self):
        # Create an initial empty tree for each test
        self.root = None

    def test_insert_into_empty_tree(self):
        self.root = insert(self.root, 100)
        self.assertEqual(self.root.key, 100)
        self.assertIsNone(self.root.left)
        self.assertIsNone(self.root.right)

    def test_insert_left_and_right(self):
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 50)  # Insert left
        self.root = insert(self.root, 150)  # Insert right
        
        self.assertEqual(self.root.key, 100)
        self.assertEqual(self.root.left.key, 50)
        self.assertEqual(self.root.right.key, 150)
        
    def test_insert_deeper_levels(self):
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 50)
        self.root = insert(self.root, 150)
        self.root = insert(self.root, 125)
        self.root = insert(self.root, 25)
        
        self.assertEqual(self.root.left.left.key, 25)  # Deep left
        self.assertEqual(self.root.right.left.key, 125)  # Deep right

    def test_handle_duplicates(self):
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 100)  # Duplicate value
        
        # Check that no duplicate node is inserted
        self.assertIsNone(self.root.left)
        self.assertIsNone(self.root.right)

    def test_large_tree(self):
        # Insert multiple values to create a larger tree
        values = [100, 50, 150, 25, 75, 125, 175]
        for value in values:
            self.root = insert(self.root, value)
        
        # Verify the tree structure
        self.assertEqual(self.root.key, 100)
        self.assertEqual(self.root.left.key, 50)
        self.assertEqual(self.root.right.key, 150)
        self.assertEqual(self.root.left.left.key, 25)
        self.assertEqual(self.root.left.right.key, 75)
        self.assertEqual(self.root.right.left.key, 125)
        self.assertEqual(self.root.right.right.key, 175)

    def test_empty_tree(self):
        # Confirm the initial root is None
        self.assertIsNone(self.root)

    def test_print_tree(self):
        # Test that `print_tree` produces output without errors
        from InsertNode import print_tree  # Import here if used in tests
        self.root = insert(self.root, 100)
        self.root = insert(self.root, 50)
        self.root = insert(self.root, 150)
        
        # Call `print_tree` to ensure no exceptions are raised
        try:
            print_tree(self.root)
        except Exception as e:
            self.fail(f"print_tree raised an exception: {e}")

if __name__ == "__main__":
    unittest.main()
