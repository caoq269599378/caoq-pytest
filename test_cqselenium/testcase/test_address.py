###po封装下，添加通讯录成员###
from test_cqselenium.cqaddress_page.cqmain_page import MainPage

class TestAddress:
    def test_add_member(self):
        main = MainPage()
        main.goto_address().add_member()