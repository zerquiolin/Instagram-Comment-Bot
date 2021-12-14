from selenium import webdriver
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option('detach', True)
chromeOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
chromeOptions.add_argument('--incognito')

class BotBuilder:
    def __init__(self, chromeDriverPath):
        self.driver = webdriver.Chrome(chromeDriverPath, chrome_options=chromeOptions)
        pass
    def goTo(self, url):
        self.driver.get(url)
    def typeOn(self, xpath, text):
        textField = self.driver.find_element_by_xpath(xpath)       
        time.sleep(1)
        textField.send_keys(text)
    def clickOn(self, xpath):
        button = self.driver.find_element_by_xpath(xpath)
        button.click()
    def quit(self):
        self.driver.quit()