import unittest

# Assume this is your application logic
def multiply(a, b):
    return a * b

# Here are your test cases
class MultiplyTestCase(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-1, 2), -2)
        self.assertEqual(multiply(0, 10), 0)

# This makes the test cases run when the file is executed
if __name__ == '__main__':
    unittest.main()