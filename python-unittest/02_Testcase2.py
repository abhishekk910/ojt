import unittest
from selenium import webdriver

class SearchEngineTest1(unittest.TestCase):
    def test_Google(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://www.google.com/")
        print("Title of page is " + self.driver.title)
        self.driver.close()


class SearchEngineTest2(unittest.TestCase):
    def test_Bing(self):
        self.driver = webdriver.Chrome(executable_path="C:\drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("https://bing.com/")
        print("Title of page is " + self.driver.title)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()