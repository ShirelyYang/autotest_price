from autotest_price.price_android.price_page.app import App


class TestYicheNumber:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().found().goto_yiche_number()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        self.app.back()

    # 选择新闻
    def test_news(self):
        title, title_detail = self.main.news()
        assert title == title_detail

    # 选择视频
    def test_video(self):
        title, title_detail = self.main.video()
        assert title == title_detail