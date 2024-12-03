import unittest
from Queue import enqueue, dequeue
class TestQueueOperations(unittest.TestCase):
    
    # Test Case 1: Test enqueue operation (inserting elements into the queue)
    def test_enqueue_elements(self):
        global queue, front, rear
        queue = [None] * 3  # Reinitialize the queue for each test case
        front = 0
        rear = 0
        
        # Enqueue "Car 1", "Car 2", and "Car 3"
        enqueue("Car 1")
        self.assertEqual(queue, ["Car 1", None, None])
        self.assertEqual(rear, 1)
        
        enqueue("Car 2")
        self.assertEqual(queue, ["Car 1", "Car 2", None])
        self.assertEqual(rear, 2)
        
        enqueue("Car 3")
        self.assertEqual(queue, ["Car 1", "Car 2", "Car 3"])
        self.assertEqual(rear, 3)

    # Test Case 2: Test enqueue when the queue is full
    def test_enqueue_when_full(self):
        global queue, front, rear
        queue = ["Car 1", "Car 2", "Car 3"]  # Reinitialize the queue as full
        front = 0
        rear = 3
        
        # Try to enqueue "Car 4" when the queue is full
        enqueue("Car 4")
        self.assertEqual(queue, ["Car 1", "Car 2", "Car 3"])
        self.assertEqual(rear, 3)
        
    # Test Case 3: Test dequeue operation (removing elements from the queue)
    def test_dequeue_elements(self):
        global queue, front, rear
        queue = ["Car 1", "Car 2", "Car 3"]
        front = 0
        rear = 3
        
        # Dequeue "Car 1"
        dequeue()
        self.assertEqual(queue, ["Car 1", "Car 2", "Car 3"])
        self.assertEqual(front, 1)
        
        # Dequeue "Car 2"
        dequeue()
        self.assertEqual(queue, ["Car 1", "Car 2", "Car 3"])
        self.assertEqual(front, 2)
        
        # Dequeue "Car 3"
        dequeue()
        self.assertEqual(queue, ["Car 1", "Car 2", "Car 3"])
        self.assertEqual(front, 3)
        
    # Test Case 4: Test dequeue when the queue is empty
    def test_dequeue_when_empty(self):
        global queue, front, rear
        queue = [None] * 3  # Reinitialize the queue as empty
        front = 0
        rear = 0
        
        # Try to dequeue when the queue is empty
        dequeue()
        self.assertEqual(queue, [None, None, None])
        self.assertEqual(front, 0)
        self.assertEqual(rear, 0)
        
    # Test Case 5: Test enqueue after dequeue operations
    def test_enqueue_after_dequeue(self):
        global queue, front, rear
        queue = ["Car 1", "Car 2", "Car 3"]
        front = 0
        rear = 3
        
        # Dequeue all elements
        dequeue()  # Dequeue "Car 1"
        dequeue()  # Dequeue "Car 2"
        dequeue()  # Dequeue "Car 3"
        
        # Enqueue a new element "Car 4"
        enqueue("Car 4")
        self.assertEqual(queue, ["Car 4", None, None])
        self.assertEqual(front, 0)
        self.assertEqual(rear, 1)

if __name__ == '__main__':
    unittest.main()
