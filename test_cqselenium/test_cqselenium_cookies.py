import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

class Testqiyeweixin:
    def setup(self):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = '127.0.0.1:9222'
        #self.driver = webdriver.Chrome(options=chrome_arg)
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()

    def test_qiyeweixin(self):
        self.driver.get("https://work.weixin.qq.com")
        self.driver.find_element(By.XPATH, "//*[@class = 'index_top_operation_loginBtn']").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//*[@class = 'login_registerBar_link']").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//*[@id = 'corp_name']").send_keys("测试人员")
        sleep(6)

    def test_cookie_login(self):
        #cookies = self.driver.get_cookies()
        #with open("tmp.txt", "w", encoding="utf-8") as f:
            #f.write(json.dumps(cookies))

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        with open("tmp.txt", "r", encoding="utf-8") as f:
            raw_cookies = f.read()
            cookies = json.loads(raw_cookies)

        for i in cookies:
            self.driver.add_cookie(i)
        self.driver.refresh()
        sleep(6)
