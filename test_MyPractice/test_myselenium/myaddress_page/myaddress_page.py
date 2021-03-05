
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class AddressPage():
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):

        def wait_name(driver):


