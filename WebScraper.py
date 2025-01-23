from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chromedriver_path = "/usr/bin/chromedriver"  
chrome_binary_path = "/usr/bin/google-chrome"  

options = webdriver.ChromeOptions()
options.binary_location = chrome_binary_path

driver = webdriver.Chrome(service=Service(chromedriver_path), options=options)
driver.get("https://example.com")
print(driver.page_source)
driver.quit()
