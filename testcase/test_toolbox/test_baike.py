from autotest_price.price_android.price_page.app import App


class TestBake:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_baike()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        self.app.back()

    def test_baike(self):
        title, topic_subject = self.main.baike()
        assert title == topic_subject

    def test_more(self):
        title = self.main.more()
        assert title == "灯泡损坏指示灯"
