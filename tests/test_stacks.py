import unittest

from stacks import Stack

class StackTestCase(unittest.TestCase):
    def test_is_empty_true(self):
        test_obj = Stack()
        self.assertEqual(True, test_obj.is_empty())

    def test_is_empty_false(self):
        test_obj = Stack()
        test_obj.push('data')
        self.assertEqual(False, test_obj.is_empty())

if __name__ == '__main__':
    unittest.main()
