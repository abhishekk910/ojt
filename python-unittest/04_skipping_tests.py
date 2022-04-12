import unittest

class TestSearch(unittest.TestCase):

    @unittest.SkipTest
    def test_login_FB(self):
        print("This is login FB test case")

    @unittest.skip("This function is not yet ready")
    def test_login_Instagram(self):
        print("This is login Instagram test case")

    @unittest.skipIf('Python' != 'Python', "Strings are not equal")
    def test_login_Twitter(self):
        print("This is login Twitter test case")

    def test_login_Gmail(self):
        print("This is login Gmail test case")

    def test_login_Udemy(self):
        print("This is login Udemy test case")


if __name__ == "__main__":
    unittest.main()