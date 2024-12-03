import unittest
from Nodeatstart import DoublyLinkedList
class TestDoublyLinkedList(unittest.TestCase):
    
    # Test Case 1: Empty List
    def test_empty_list(self):
        dll = DoublyLinkedList()
        # Test if the list is empty, no output is expected
        self.assertIsNone(dll.head)
    
    # Test Case 2: Adding a Single Node
    def test_add_single_node(self):
        dll = DoublyLinkedList()
        dll.add_first(10)
        # The list should only have one node with value 10
        current = dll.head
        self.assertEqual(current.val, 10)
        self.assertIsNone(current.next)
        self.assertIsNone(current.prev)
    
    # Test Case 3: Adding Multiple Nodes
    def test_add_multiple_nodes(self):
        dll = DoublyLinkedList()
        dll.add_first(10)
        dll.add_first(20)
        dll.add_first(30)
        # The list should contain nodes in the reverse order: 30 <-> 20 <-> 10
        current = dll.head
        self.assertEqual(current.val, 30)
        self.assertEqual(current.next.val, 20)
        self.assertEqual(current.next.next.val, 10)
    
    # Test Case 4: Adding More Nodes
    def test_add_more_nodes(self):
        dll = DoublyLinkedList()
        dll.add_first(100)
        dll.add_first(200)
        dll.add_first(300)
        # The list should contain nodes in the reverse order: 300 <-> 200 <-> 100
        current = dll.head
        self.assertEqual(current.val, 300)
        self.assertEqual(current.next.val, 200)
        self.assertEqual(current.next.next.val, 100)

    # Test Case 5: Adding Nodes After an Empty List
    def test_add_nodes_after_empty_list(self):
        dll = DoublyLinkedList()
        dll.add_first(1)
        dll.add_first(2)
        dll.add_first(3)
        # The list should contain nodes in the reverse order: 3 <-> 2 <-> 1
        current = dll.head
        self.assertEqual(current.val, 3)
        self.assertEqual(current.next.val, 2)
        self.assertEqual(current.next.next.val, 1)

    # Test Case 6: Adding Nodes and Printing
    def test_add_and_print_nodes(self):
        dll = DoublyLinkedList()
        dll.add_first(5)
        dll.add_first(15)
        dll.add_first(25)
        dll.add_first(35)
        # The list should contain nodes in the reverse order: 35 <-> 25 <-> 15 <-> 5
        current = dll.head
        self.assertEqual(current.val, 35)
        self.assertEqual(current.next.val, 25)
        self.assertEqual(current.next.next.val, 15)
        self.assertEqual(current.next.next.next.val, 5)

if __name__ == '__main__':
    unittest.main()
