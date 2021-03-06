###在企业微信添加通讯录###

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestTmp():
    def test_address(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, "//*[@id='menu_contacts']").click()

        def wait_name(driver):
            driver.find_elements(By.XPATH, "//*[@class= 'qui_btn ww_btn js_add_member']")[1].click()
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_name)

        self.driver.find_element(By.XPATH, "//*[@id = 'username']").send_keys("测试人员1")
        self.driver.find_element(By.XPATH, "//*[@id = 'memberAdd_acctid']").send_keys("happy")
        self.driver.find_element(By.XPATH, "//*[@id = 'memberAdd_phone']").send_keys("12345678901")
        self.driver.find_element(By.XPATH, "//*[@class = 'qui_btn ww_btn js_btn_save']").click()


