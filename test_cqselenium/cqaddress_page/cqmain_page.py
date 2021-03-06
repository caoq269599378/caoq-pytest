from selenium import webdriver
from selenium.webdriver.common.by import By

from test_cqselenium.cqaddress_page.cqaddress_page import AddressPage


class MainPage:
    def __init__(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)

    def goto_address(self):
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        return AddressPage(self.driver)