from time import sleep
from selenium import webdriver

class MyBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://google.com")
        self.driver.maximize_window()
        print(self.driver.title)
        sleep(5)

MyBot()
