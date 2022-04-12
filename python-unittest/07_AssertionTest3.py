import unittest


class Test(unittest.TestCase):
    def test_func1(self):
        a = None
        self.assertIsNotNone(a)

if __name__ == "__main__":
    unittest.main()