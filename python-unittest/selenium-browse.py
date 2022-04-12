from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

s=Service('C:\drivers\chromedriver_win32\chromedriver.exe')

driver = webdriver.Chrome(service=s)

url='https://www.google.com'
driver.get(url)
print(driver.title)

driver.close()