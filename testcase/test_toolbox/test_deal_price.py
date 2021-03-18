from autotest_price.price_android.price_page.app import App


class TestDealPrice:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_deal_price()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    # 成交价格
    def test_deal_award(self):
        luoche_price = self.main.deal_price()
        assert luoche_price == "8.9万"
        self.app.back()

    # 询底价
    def test_askprice(self):
        askprice_btn = self.main.ask_price()
        assert askprice_btn == "获取底价"
        self.app.back()

    # 说明
    def test_description(self):
        toast = self.main.description()
        assert toast == "非发票形式获取，仅供参考"

    # 查看发票
    def test_invoice(self):
        img = self.main.invoice()
        assert img == True
        self.app.back()

    # 其他城市
    def test_other_city(self):
        city = self.main.other_city()
        assert city == "武汉"

    # 落地价-全款
    def test_full_amount(self):
        total_price, fullPaymentTxt = self.main.full_amount()
        assert total_price == fullPaymentTxt + "元"

    # 落地价-贷款
    def test_loan(self):
        total_price_loan, zjTxt = self.main.loan()
        assert total_price_loan == zjTxt + "元"

    # 保值率
    # def test_rate(self):
    #     sales_ratio_tv, rate = self.main.rate()
    #     assert rate in sales_ratio_tv