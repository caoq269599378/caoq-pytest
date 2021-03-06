from test_cqselenium.cqlogin_page.cqmain_page import MainPage


class TestRegister:
    def test_register(self):
        main = MainPage()
        main.goto_register().register()
