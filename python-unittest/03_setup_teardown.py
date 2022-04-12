import unittest

def setUpModule():
    print("setUp Module")

def tearDownModule():
    print("tear Down Module")

class AppTesting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Open Browser")

    @classmethod
    def tearDownClass(cls):
        print("Close Browser")

    @classmethod
    def setUp(self):
        print("Please Login")

    @classmethod
    def tearDown(self):
        print("Logged out")

    def test_facebook(self):
        print("Loggined in into facebook website")

    def test_instagram(self):
        print("Loggined in into instagram website")

    def test_udemy(self):
        print("Loggined in into udemy website")

if __name__ == "__main__":
    unittest.main()