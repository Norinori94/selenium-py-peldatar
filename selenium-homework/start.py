from selenium import webdriver

url = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome()

browser.get("https://www.google.com/")
browser.quit()

