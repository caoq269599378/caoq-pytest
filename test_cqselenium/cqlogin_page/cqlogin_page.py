from selenium.webdriver.common.by import By

from test_cqselenium.cqlogin_page.cqregister_page import RegisterPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='login_registerBar_link']").click()
        return RegisterPage(self.driver)

    def scan(self):
        pass
