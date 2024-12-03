import unittest
from Searching import DoublyLinkedList, Node
class TestDoublyLinkedList(unittest.TestCase):
    
    # Test Case 1: Search in an Empty List
    def test_search_empty_list(self):
        dll = DoublyLinkedList()
        # Search for any node in an empty list should return False
        self.assertFalse(dll.search_node(10))
    
    # Test Case 2: Search for a Node that Exists
    def test_search_existing_node(self):
        dll = DoublyLinkedList()
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        dll.head = node1
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        
        # Searching for a node that exists (30)
        self.assertTrue(dll.search_node(30))
    
    # Test Case 3: Search for a Node that Does Not Exist
    def test_search_non_existing_node(self):
        dll = DoublyLinkedList()
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        dll.head = node1
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        
        # Searching for a node that does not exist (40)
        self.assertFalse(dll.search_node(40))
    
    # Test Case 4: Search After Adding Nodes to the List
    def test_search_after_adding_nodes(self):
        dll = DoublyLinkedList()
        dll.search_node(10)  # Search in an empty list
        node1 = Node(10)
        node2 = Node(20)
        dll.head = node1
        node1.next = node2
        node2.prev = node1
        
        # Search for a node that exists (20)
        self.assertTrue(dll.search_node(20))
        
        # Search for a node that does not exist (30)
        self.assertFalse(dll.search_node(30))
    
    # Test Case 5: Search in a List with Multiple Nodes
    def test_search_multiple_nodes(self):
        dll = DoublyLinkedList()
        node1 = Node(10)
        node2 = Node(20)
        node3 = Node(30)
        node4 = Node(40)
        
        dll.head = node1
        node1.next = node2
        node2.prev = node1
        node2.next = node3
        node3.prev = node2
        node3.next = node4
        node4.prev = node3
        
        # Search for an existing node (20)
        self.assertTrue(dll.search_node(20))
        
        # Search for a non-existing node (50)
        self.assertFalse(dll.search_node(50))

if __name__ == '__main__':
    unittest.main()
