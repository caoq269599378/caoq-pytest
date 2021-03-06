from selenium import webdriver
from selenium.webdriver.common.by import By

from test_cqselenium.cqlogin_page.cqlogin_page import LoginPage
from test_cqselenium.cqlogin_page.cqregister_page import RegisterPage


class MainPage:
    def __init__(self):
        #chrome_arg = webdriver.ChromeOptions()
        #chrome_arg.debugger_address = '127.0.0.1:9222'
        #self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com")

    def goto_register(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_head_info_pCDownloadBtn']").click()
        #将类初始化成对象
        return RegisterPage(self.driver)

    def goto_login(self):
        self.driver.find_element(By.XPATH, "//*[@class='index_top_operation_loginBtn']").click()
        return LoginPage(self.driver)

    def goto_download(self):
        pass

