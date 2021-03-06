###po封装下，cqlogin_page的测试用例###

from time import sleep
from test_cqselenium.cqlogin_page.cqmain_page import MainPage

class TestRegister:
    def test_register(self):
        main = MainPage()
        main.goto_register().register()
        sleep(5)

    def test_login_register(self):
        main = MainPage()
        main.goto_login().goto_register().register()
        sleep(5)

