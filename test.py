from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='geckodriver.exe')
driver.get("https://google.com/")
print ("Headless Firefox Initialized")
driver.quit ()