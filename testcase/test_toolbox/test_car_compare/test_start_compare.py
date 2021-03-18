from autotest_price.price_android.price_page.app import App


class TestStartCompare:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_model_comparison()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    def test_add_recommended_models(self):
        car_name, compare_car_name = self.main.add_recommended_models()
        assert car_name in compare_car_name

    def test_edit_all_del(self):
        empty_info = self.main.edit_all_del()
        assert empty_info == "暂无对比车款"