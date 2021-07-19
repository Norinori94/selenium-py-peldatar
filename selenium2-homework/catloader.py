'''
023 Feladat: Load more feladatok
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/loadmore.html oldalt.
Mentsd le az első 20 macskás képet az oldalról. A fájlokat egy külön cats könyvtárba mentsd le.
A fájlneve legyen a következő {sorszam}_{cat_id} ahol a sorszám alatt azt értjük, hogy hanyadiknak lett megjelenítve és cat_id meg az azonosító amit szolgáltató ad.
A {} jelek ne legyenek benne a fájlnévben.
'''
import time
from selenium import webdriver

path = "C://Windows//chromedriver.exe"
url = "http://localhost:9999/loadmore.html"
browser = webdriver.Chrome(path)

try:
    browser.get(url)
    browser.maximize_window()

    button_more_images = browser.find_element_by_xpath('//button[text()="More Images"]')

    button_more_images.click()
    button_more_images.click()
    button_more_images.click()
    time.sleep(5)
    cat_ids = browser.find_elements_by_xpath('//div[@class="image"]/p')
    images = browser.find_elements_by_xpath('//div[@class="image"]/img')

    count = 1

    for i in images:
        cat_id = cat_ids[count - 1].text[8:]
        image_name = str(count) + "_" + cat_id
        with open(f'cats/{image_name}.png', 'wb') as file:
            file.write(images[count - 1].screenshot_as_png)
        count += 1
except:
    print("Something wrong.")
finally:
    browser.quit()
