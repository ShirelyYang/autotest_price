from autotest_price.price_android.price_page.app import App


class TestHeadlines:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().found().goto_headlines()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    # 专题
    def test_special(self):
        is_enabled = self.main.special()
        assert is_enabled == True
        self.app.back()

    # 资讯
    def test_news(self):
        news_title, topic_subject = self.main.news()
        assert news_title in topic_subject
        self.app.back()

    # 广告
    def test_adver(self):
        is_enabled = self.main.adver()
        # print(is_enabled)
        if is_enabled == "没有广告":
            assert is_enabled == "没有广告"
        else:
            assert is_enabled == True
        self.app.back()

    # 小视频
    def test_small_video(self):
        title, title_detail = self.main.small_video()
        if title == "头条tab下没有小视频":
            assert title_detail == "头条tab下没有小视频"
        else:
            assert title_detail == title
        self.app.back()

    # 动态
    def test_dynamic(self):
        content, content_lis = self.main.dynamic()
        assert content_lis in content
        self.app.back()

    # 动态点赞
    def test_dynamic_like(self):
        count, count_like = self.main.dynamic_like()
        assert count_like == (count + 1)

    # 动态-评论
    def test_dynamic_comment(self):
        comment, comment_content = self.main.dynamic_comment()
        assert comment == comment_content
        self.app.back()

    # 动态-销售详情
    def test_dynamic_sales_detail(self):
        name, sale_name = self.main.dynamic_sales_detail()
        assert name == sale_name
        self.app.back()

    # 动态-销售红包
    def test_dynamic_red_packet(self):
        title = self.main.dynamic_red_packet()
        assert title == "限时领取"
        self.app.back()

    # 动态-动态详情-微聊
    def test_dynamic_detail_chat(self):
        sale_name, title = self.main.dynamic_detail_chat()
        assert sale_name in title
        self.app.back()

    # 动态详情-图片放大
    def test_dynamic_list_picture(self):
        msg = self.main.dynamic_list_picture()
        assert msg == "已保存到相册"
        self.app.back()

    # 视频-播放
    def test_video_start(self):
        start = self.main.video_start()
        assert start == False

    # 视频-详情
    def test_video_detail(self):
        title, title_detail = self.main.video_detail()
        assert title == title_detail
        self.app.back()

    # 资讯-关联车型
    def test_news_serial_name(self):
        news_serial_name, brandtype_serial_name = self.main.news_serial_name()
        assert brandtype_serial_name in news_serial_name
        self.app.back()

    # 新车-新闻详情页-车型链接
    def test_news_detail_car_link(self):
        car, brand_car = self.main.news_detail_car_link()
        assert car == brand_car
        self.app.back()

    # 新闻详情页 - 参数链接
    def test_news_detail_parameter_link(self):
        notice = self.main.news_detail_parameter_link()
        assert notice == "注：以上仅供参考，请以店内实车为准"
        self.app.back()

    # 新闻详情页 - 询价链接
    def test_news_detail_ask_price_link(self):
        btn = self.main.news_detail_ask_price_link()
        assert btn == "获取底价"
        self.app.back()

    # 新闻详情页 - 图片链接
    def test_news_detail_picture_link(self):
        msg = self.main.news_detail_picture_link()
        assert msg == "已保存到相册"