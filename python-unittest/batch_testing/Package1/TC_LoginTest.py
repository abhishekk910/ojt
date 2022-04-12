import unittest

class LoginTest(unittest.TestCase):

    def test_loginEmail(self):
        print("This is Login Email Test")
        self.assertTrue(True)

    def test_loginFB(self):
        print("This is Login FB Test")
        self.assertTrue(True)

    def test_loginTwitter(self):
        print("This is Login Twitter Test")
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()