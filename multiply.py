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


class MultiplyEdgeCasesTestCase(unittest.TestCase):
    def test_multiply_with_zero(self):
        self.assertEqual(multiply(0, 10), 0)
        self.assertEqual(multiply(0, 0), 0)
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_with_negatives(self):
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(-1, 2), -2)
        self.assertEqual(multiply(3, -4), -12)

# This makes the test cases run when the file is executed
if __name__ == '__main__':
    unittest.main()
