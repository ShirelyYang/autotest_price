from autotest_price.price_android.price_page.app import App


class TestBorrowCash:
    def setup(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_borrow_cash()

    def teardown(self):
        self.app.base_quit()

    # 借现金
    def test_borrow_cash(self):
        title = self.main.borrow_cash()
        assert title == "度小满金融"
