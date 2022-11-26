from time import sleep
from selenium import webdriver
import os

class MyBot:
    def __init__(self):
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; \
        x64) AppleWebKit/537.36 (KHTML, like Gecko) \
        Chrome/107.0.0.0 Safari/537.36"

        self.options = webdriver.ChromeOptions()
        self.options.headless = True
        self.options.add_argument(f'user-agent={user_agent}')
        self.options.add_argument("--window-size=1920,1080")
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--allow-running-insecure-content')
        self.options.add_argument("--disable-extensions")
        self.options.add_argument("--proxy-server='direct://'")
        self.options.add_argument("--proxy-bypass-list=*")
        self.options.add_argument("--start-maximized")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--no-sandbox')
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe", options=self.options)


        self.driver.get("https:///google.com")
        self.driver.get_screenshot_as_file("Screenshot.png")
        print(self.driver.title)
MyBot()


# Another way to add chromewebdriver 
# 1. pip install chromedriver-binary
# 2. import the package

# from selenium import webdriver
# import chromedriver_binary  #(Adds chromedriver binary to path)

# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
