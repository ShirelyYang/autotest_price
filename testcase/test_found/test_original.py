from autotest_price.price_android.price_page.app import App


class TestOriginal:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().found().goto_original()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        # self.app.back()
        pass

    # 查看新闻详情页的图片大图
    # def test_new_car_detail_big_picture(self):
    #     msg = self.main.new_car_detail_big_picture()
    #     assert msg == "已保存到相册"

    # 点击新闻详情页相关推荐-车型
    def test_new_car_detail_recommend_car(self):
        car_name, brand_car = self.main.new_car_detail_recommend_car()
        assert brand_car in car_name

    # 点击新闻详情页相关推荐-询底价
    def test_new_car_detail_recommend_ask_price(self):
        btn = self.main.new_car_detail_recommend_ask_price()
        assert btn == "获取底价"

    # 点击新闻详情页相关推荐-资讯
    def test_new_car_detail_recommend_news(self):
        news_title, title = self.main.new_car_detail_recommend_news()
        assert title in news_title

    # 点击新闻详情页-评论
    def test_new_car_detail_comment(self):
        msg = self.main.new_car_detail_comment()
        assert msg == "评论成功!"

    # 点击新闻详情页-查看全部评论
    def test_new_car_detail_comment_all(self):
        comment = self.main.new_car_detail_comment_all()
        assert comment == "不错诶"

    # 点击新闻详情页-收藏
    def test_new_car_detail_collection(self):
        lis = ["收藏成功", "已取消收藏"]
        msg = self.main.new_car_detail_collection()
        assert msg in lis

    # 点击新闻详情页-分享
    def test_new_car_detail_share(self):
        weixin = self.main.new_car_detail_share()
        assert weixin == "微信好友"

    # 点击新闻详情页-看车
    def test_new_car_detail_look_car(self):
        car_name, brand_name = self.main.new_car_detail_look_car()
        assert car_name == brand_name

    # 点击新闻详情页-询底价
    def test_new_car_detail_look_car_ask_price(self):
        btn = self.main.new_car_detail_look_car_ask_price()
        assert btn == "获取底价"

    # 点击新闻详情页-看车-参数配置
    def test_new_car_detail_look_car_parameter(self):
        notice = self.main.new_car_detail_look_car_parameter()
        assert notice == "注：以上仅供参考，请以店内实车为准"

    # 点击新闻详情页-看车-图片
    def test_new_car_detail_look_car_picture(self):
        msg = self.main.new_car_detail_look_car_picture()
        assert msg == "已保存到相册"

    # 点击新闻详情页-看车-最新资讯
    def test_new_car_detail_look_car_news(self):
        status = self.main.new_car_detail_look_car_news()
        assert status == True

    # 点击新闻详情页-看车-车款列表
    def test_new_car_detail_look_car_cartypelist(self):
        status = self.main.new_car_detail_look_car_cartypelist()
        assert status == True

    # 评论数大于20条的新闻详情-新增主评论
    # def test_add_comment(self):
    #     content, content_send = self.main.add_comment()
    #     assert content == content_send

    # 进入评测tab
    def test_goto_evaluating(self):
        title, title_detail = self.main.goto_evaluating()
        assert title == title_detail

    # 进入导购tab
    def test_goto_shopping(self):
        title, title_detail = self.main.goto_shopping()
        assert title == title_detail

    # 进入图片tab
    def test_goto_picture(self):
        title, title_detail = self.main.goto_picture()
        assert title == title_detail

    # 图片新闻列表页 查看图片大图
    def test_list_picture(self):
        msg = self.main.list_picture()
        assert msg == "已保存到相册"