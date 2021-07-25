from selenium import webdriver
from selenium.webdriver import ActionChains


class TestAlertPlayground:

    def setup(self):
        self.driver = webdriver.Chrome("C://Windows//chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("http://localhost:9999/alert_playground.html")

    def teardown(self):
        self.driver.quit()

    def test_alert_button_ok(self):
        self.driver.find_element_by_xpath('//input[@name="alert"]').click()
        alert_pop = self.driver.switch_to.alert
        assert alert_pop.text == "I am alert"
        alert_pop.accept()

    def test_confirmation_box_ok(self):
        self.driver.find_element_by_xpath('//input[@name="confirmation"]').click()
        alert_pop = self.driver.switch_to.alert
        assert alert_pop.text == "I am confirm"
        alert_pop.accept()

    def test_confirmation_box_megse(self):
        self.driver.find_element_by_xpath('//input[@name="confirmation"]').click()
        alert_pop = self.driver.switch_to.alert
        assert alert_pop.text == "I am confirm"
        alert_pop.dismiss()

    def test_prompt_megse(self):
        self.driver.find_element_by_xpath('//input[@name="prompt"]').click()
        alert_pop = self.driver.switch_to.alert
        assert (alert_pop.text == "I am prompt")
        alert_pop.send_keys("Teszt")
        alert_pop.dismiss()
        assert self.driver.find_element_by_id("demo").text == ""

    def test_prompt_ok(self):
        self.driver.find_element_by_xpath('//input[@name="prompt"]').click()
        alert_pop = self.driver.switch_to.alert
        alert_pop.send_keys("Teszt")
        alert_pop.accept()
        assert self.driver.find_element_by_id("demo").text == "You entered: Teszt"

    def test_prompt_ok_fail(self):
        self.driver.find_element_by_xpath('//input[@name="prompt"]').click()
        alert_pop = self.driver.switch_to.alert
        alert_pop.send_keys("Teszt")
        alert_pop.accept()
        assert self.driver.find_element_by_id("demo").text == "You entered: Teszt fail"

    def test_double_click_me_ok(self):
        action = ActionChains(self.driver)
        action.double_click(on_element=self.driver.find_element_by_id("double-click"))
        action.perform()
        alert_pop = self.driver.switch_to.alert
        assert alert_pop.text == "You double clicked me!!!, You got to be kidding me"
        alert_pop.accept()
