from selenium import webdriver

path = ("C:\\Windows\\chromedriver.exe")
url = "https://www.google.com/"
browser = webdriver.Chrome(path)

browser.get(url)
browser.maximize_window()

def find_by_id_hibakezeles(id):
    try:
        browser.find_element_by_id(id)
    except:
        print("Nem található az általad megadott elem.")

find_by_id_hibakezeles("nemletezik")
browser.quit()
