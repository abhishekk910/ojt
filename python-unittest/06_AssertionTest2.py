import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def test_func1(self):
        a = 1
        b = 1
        self.assertTrue(a == b)
        # self.assertFalse(a != b)

    def test_webpage(self):
        driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        Title_webpage = driver.title
        self.assertFalse("Google" == Title_webpage)
        # self.assertFalse("Google123" == Title_webpage)

if __name__ == "__main__":
    unittest.main()