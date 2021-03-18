from autotest_price.price_android.price_page.app import App


class TestCommentList:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_sales_ranking()

    def teardown_class(self):
        self.app.base_quit()

    def setup(self):
        pass

    def teardown(self):
        self.app.back()

    def test_sales_list(self):
        type = self.main.sales_list()
        assert type == "国产/中大型SUV"

    def test_comment_list(self):
        type = self.main.comment_list()
        assert type == "进口/中大型SUV"

    def test_popularity_list(self):
        type = self.main.popularity_list()
        assert type == "进口/中大型SUV"

    def test_rank_residualratio(self):
        type = self.main.rank_residualratio_list()
        assert type == "进口/中大型SUV"

