from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTmp():
    def test_address(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)

        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()
        self.driver.find_element(By.XPATH, "//*[@class= 'qui_btn ww_btn js_add_member']").click()
        self.driver.find_element(By.XPATH, "//*[@id = 'username']").send_keys("测试人员1")
        self.driver.find_element(By.XPATH, "//*[@id = 'memberAdd_acctid']").send_keys("happy")
        self.driver.find_element(By.XPATH, "//*[@id = 'memberAdd_phone']").send_keys("12345678901"
        self.driver.find_element(By.XPATH, "//*[@class = 'qui_btn ww_btn js_btn_save']").click()
