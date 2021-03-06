from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class AddressPage:
    def __init__(self, driver):
        self.driver = driver

    def add_member(self):
        def wait_name(driver):
            driver.find_elements(By.XPATH, "//*[@class= 'qui_btn ww_btn js_add_member']")[1].click()
            eles = driver.find_elements(By.XPATH, "//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles) > 0
        WebDriverWait(self.driver, 10).until(wait_name)

        self.driver.find_element(By.XPATH, "//*[@id = 'username']").send_keys("测试人员2")
        self.driver.find_element(By.XPATH, "//*[@id = 'memberAdd_acctid']").send_keys("happy")
        self.driver.find_element(By.XPATH, "//*[@id = 'memberAdd_phone']").send_keys("12345678901")
        self.driver.find_element(By.XPATH, "//*[@class = 'qui_btn ww_btn js_btn_save']").click()
