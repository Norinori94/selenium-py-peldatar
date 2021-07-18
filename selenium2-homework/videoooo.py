'''
019 Feladat: videó lejátszás kihívások
Készíts egy Python alkalmazást ami selenium-ot használ.
Indítsd el lokálisan a selenium-py-peldatar alkalmazást.
A program töltse be a példatárból az http://localhost:9999/videos.html oldalt.
Az oldalon találhotó összes beágyazott videót indítsa el és állítsa meg.
'''
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def star_video(id):
    video = browser.find_element_by_id(id)
    video.click()
    video.send_keys(Keys.SPACE)
    time.sleep(2)
    video.send_keys(Keys.SPACE)


path = "C://Windows//chromedriver.exe"
url = "http://localhost:9999/videos.html"
browser = webdriver.Chrome(path)

try:
    browser.get(url)
    browser.maximize_window()

    # 1. videó lejátszása
    star_video("html5video")

    # 2. videó lejátszása
    button_play_pause = browser.find_element_by_xpath('//button[@onclick="playPause()"]')
    button_play_pause.click()
    time.sleep(2)
    button_play_pause.click()

    # 3. videó lejátszása
    star_video("youtubeframe")
    browser.find_element_by_id("youtubeframe").click()
except:
    print("Something went wrong.")

finally:
    browser.quit()
