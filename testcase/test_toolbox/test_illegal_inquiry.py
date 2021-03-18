from autotest_price.price_android.price_page.app import App


class TestIllegalInquiry:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_illegal_inquiry()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    # 查看详情-查看罚款
    def test_detail_fine(self):
        fine = self.main.details_fine()
        assert fine == "200"
        self.app.back()

    # 查看详情-代缴
    def test_detail_pay(self):
        title = self.main.details_pay()
        assert title == "上传相关证件复印件照片"
        self.app.back()

    # 查看详情-处罚判决书
    def test_details_judgement(self):
        title = self.main.details_judgement()
        assert title == "汽车报价大全"
        self.app.back()

    # 违章查询
    def test_illegal_inquiry(self):
        fine = self.main.illegal_inquiry()
        assert fine == "200"
        self.app.back()

    # 添加车辆
    def test_add(self):
        number = self.main.add()
        assert number == "GD2126"

    # 删除
    def test_delete(self):
        numbers = self.main.delete()
        assert "GD2126" not in numbers