import unittest
from Arrays import SimpleArray, demonstrate_time_complexity

class TestTimeComplexity(unittest.TestCase):
    def test_constant_time(self):
        result = demonstrate_time_complexity()
        self.assertEqual(result["constant_time_operations"]["first_element"], 0)
        self.assertEqual(result["constant_time_operations"]["last_element"], 999)
        
    def test_linear_time(self):
        result = demonstrate_time_complexity()
        self.assertEqual(result["linear_time_operation"]["found_index"], 500)
        self.assertEqual(result["linear_time_operation"]["target_value"], 500)

class TestSimpleArray(unittest.TestCase):
    def setUp(self):
        self.array = SimpleArray()
        
    def test_add_and_get(self):
        self.assertTrue(self.array.add(5))
        self.assertEqual(self.array.get(0), 5)
        self.assertTrue(self.array.add(10))
        self.assertEqual(self.array.get(1), 10)
        
    def test_invalid_get(self):
        self.assertIsNone(self.array.get(0))
        self.array.add(5)
        self.assertIsNone(self.array.get(1))
        self.assertIsNone(self.array.get(-1))
        
    def test_remove(self):
        self.array.add(5)
        self.array.add(10)
        self.array.add(15)
        
        self.assertTrue(self.array.remove(1))
        self.assertEqual(self.array.get(0), 5)
        self.assertEqual(self.array.get(1), 15)
        
    def test_invalid_remove(self):
        self.assertFalse(self.array.remove(0))
        self.array.add(5)
        self.assertFalse(self.array.remove(1))
        self.assertFalse(self.array.remove(-1))
        
    def test_length(self):
        self.assertEqual(self.array.length(), 0)
        self.array.add(5)
        self.assertEqual(self.array.length(), 1)
        self.array.add(10)
        self.assertEqual(self.array.length(), 2)
        self.array.remove(0)
        self.assertEqual(self.array.length(), 1)
        
    def test_search(self):
        self.array.add(5)
        self.array.add(10)
        self.array.add(15)
        
        self.assertEqual(self.array.search(10), 1)
        self.assertEqual(self.array.search(5), 0)
        self.assertEqual(self.array.search(15), 2)
        self.assertEqual(self.array.search(20), -1)

if __name__ == '__main__':
    unittest.main()
