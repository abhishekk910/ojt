import unittest


class Test(unittest.TestCase):
    def test_func1(self):
        list1 = ["Python", "unittest", "pytest"]
        self.assertNotIn("python", list1)

    def test_func2(self):

        self.assertLessEqual(1001, 100)
        # self.assertGreaterEqual()


if __name__ == "__main__":
    unittest.main()