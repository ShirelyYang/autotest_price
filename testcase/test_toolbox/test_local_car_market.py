from autotest_price.price_android.price_page.app import App


class TestLocalCarMarket:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().my().more().goto_local_car_market()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    # 切换城市
    def test_change_city(self):
        info = self.main.change_city()
        assert info == "获取底价"

    # 本地优惠
    def test_local_offer(self):
        discount, activity = self.main.local_offer()
        assert activity in discount
        self.app.back()

    # 金牌顾问-详情
    def test_gold_advisor_details(self):
        name, sale_name = self.main.gold_advisor_details()
        assert name == sale_name
        self.app.back()

    # 金牌顾问-更多
    def test_gold_advisor_more(self):
        name, name_more = self.main.gold_advisor_more()
        assert name == name_more
        self.app.back()

    # 金牌顾问-附近门店-详情
    # def test_nearby_stores_details(self):
    #     store_name, dealer_name = self.main.nearby_stores_details()
    #     assert dealer_name in store_name
    #     self.app.back()

    # 金牌顾问-附近门店-销售详情
    # def test_nearby_advisor_details(self):
    #     name, sale_name = self.main.nearby_advisor_details()
    #     assert name == sale_name
    #     self.app.back()

    # 金牌顾问-附近门店-导航
    # def test_nearby_stores_map(self):
    #     addr, addr_map = self.main.nearby_stores_map()
    #     assert addr_map in addr
    #     self.app.back()

    # 金牌顾问-附近门店-更多
    # def test_nearby_stores_more(self):
    #     addr, addr_more = self.main.nearby_stores_more()
    #     assert  addr in addr_more
    #     self.app.back()

    # 金牌顾问-选择品牌
    def test_gold_advisor_brand(self):
        dealer_name = self.main.gold_advisor_brand()
        assert "奔驰" in dealer_name
        self.app.back()

    # 小视频
    def test_small_video(self):
        user_name, sale_name = self.main.small_video()
        assert user_name == sale_name
        self.app.back()

    # 4S保养-详情
    def test_maintenance(self):
        title = self.main.maintenance()
        assert title == "保养套餐详情"
        self.app.back()

    # 4S保养-马上抢
    def test_grab(self):
        title = self.main.grab()
        assert title == "填写保养信息"
        self.app.back()

    # 4S预约
    def test_booking(self):
        title = self.main.booking()
        assert title == "填写预约信息"
        self.app.back()

    # 本地成交价
    def test_deal_price(self):
        car, car_name = self.main.del_price()
        assert car in car_name

    # 本地热榜
    def test_hot_list_car(self):
        car_name, car_brandtype_serial_name = self.main.hot_list_car()
        assert car_name == car_brandtype_serial_name

    def test_hot_list_suv(self):
        suv_name, suv_brandtype_serial_name = self.main.hot_list_suv()
        assert suv_name == suv_brandtype_serial_name

    def test_hot_list_mpv(self):
        mpv_name, mpv_brandtype_serial_name = self.main.hot_list_mpv()
        assert mpv_name == mpv_brandtype_serial_name

    def test_hot_list_new_energy(self):
        new_energy_name, new_energy_brandtype_serial_name = self.main.hot_list_new_energy()
        assert new_energy_name == new_energy_brandtype_serial_name

    def test_hot_list_ask_price(self):
        info = self.main.hot_list_ask_price()
        assert info == "获取底价"

    # 糖豆-附近经销商
    def test_nearby_dealers(self):
        dealer_name, dealer_detail = self.main.nearby_dealers()
        assert dealer_detail in dealer_name
        self.app.back()

    # 糖豆-二手车
    def test_second_hand_car(self):
        car_name, fulTvName = self.main.second_hand_car()
        assert car_name == fulTvName
        self.app.back()

    # 糖豆-本地降价
    def test_price_cut(self):
        car_name, brand = self.main.price_cut()
        assert car_name == brand
        self.app.back()
