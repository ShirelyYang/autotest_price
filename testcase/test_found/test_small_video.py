from autotest_price.price_android.price_page.app import App


class TestSmallVideo:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().found().goto_small_video()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        self.app.back()

    # 收藏
    def test_collection(self):
        collection = self.main.collection()
        assert collection == True

    # 更多分享分享
    def test_more_share(self):
        weixin = self.main.more_share()
        assert weixin == "微信好友"

    # 进入销售详情页面
    def test_sale_detail(self):
        sale_name, name = self.main.goto_sale_detail()
        assert sale_name == name

    # 销售详情页-微聊
    def test_sale_detail_chat(self):
        name, title = self.main.sale_detail_chat()
        assert name in title

    # 销售详情页-关注
    def test_sale_detail_focus(self):
        msg = self.main.sale_detail_focus()
        assert msg == "已关注"

    # 销售详情页-查看粉丝
    def test_sale_detail_fans(self):
        name = self.main.sale_detial_fans()
        assert name == "大全儿6359微博"

    # 销售详情页-话题-点赞
    def test_sale_detail_like(self):
        count, count_like = self.main.sale_detail_topic_like()
        assert count_like == (count + 1)

    # 销售详情页-话题-评论
    def test_sale_detail_comment(self):
        msg = self.main.sale_detail_topic_comment()
        assert msg == "评论成功，已进入审核"

    # 销售详情页-话题-关联车型
    def test_sale_detail_topic_car(self):
        car_name, brandtype_serial_name = self.main.sale_detail_topic_car()
        assert car_name == brandtype_serial_name

    # 销售详情页-TA的评论
    def test_sale_detail_salecomment(self):
        info = self.main.sale_detail_salecomment()
        assert info == "TA还没有发表过评论"

    # 销售详情页-发布话题
    def test_sale_detail_post_topic(self):
        msg = self.main.sale_datail_post_topic()
        assert msg == "话题发表中…"

    # 小视频详情页-点赞
    def test_small_video_like(self):
        count, count_like = self.main.small_video_like()
        assert count_like == (count + 1)

    # 小视频详情页-评论
    def test_small_video_comment(self):
        msg = self.main.small_video_comment()
        assert msg == "聊一聊你的想法吧~"

    # 小视频详情页-分享
    def test_small_video_share(self):
        pyq = self.main.small_video_share()
        assert pyq == "朋友圈"

    # 小视频详情页-询底价, 有接口逻辑，暂不做UI自动化
    # def test_small_video_ask_price(self):
    #     ask_btn = self.main.small_video_ask_price()
    #     assert ask_btn == "获取底价"

    # 小视频详情页-微聊
    def test_small_video_chat(self):
        sale_name, title = self.main.small_video_chat()
        assert sale_name in title

    # 经销商详情页-地图导航
    def test_dealer_detail_map(self):
        addr, addr_map = self.main.dealer_detail_map()
        assert addr_map in addr

     # 经销商详情页-推荐销售
    def test_dealer_detail_sale(self):
        name, sale_name = self.main.dealer_detail_sale()
        assert name == sale_name

    # 经销商详情页-经销商小视频
    def test_dealer_detail_small_video(self):
        video_title, title = self.main.dealer_detail_small_video()
        assert  video_title in title

    # 经销商详情页-贷款
    def test_dealer_detail_loan(self):
        btn = self.main.dealer_detail_loan()
        assert btn == "申请贷款"

    # 经销商详情页-预约保养
    def test_dealer_detail_appointment(self):
        title = self.main.dealer_detail_appointment()
        assert title == "填写预约信息"

    # 经销商详情页-获取底价
    def test_dealer_detail_ask_price(self):
        btn = self.main.dealer_detail_ask_price()
        assert btn == "获取底价"

    # 小视频详情页-暂停播放
    def test_smal_video_stop(self):
        status = self.main.smal_video_stop()
        assert status == True

    # 小视频tab-发布小视频
    # def test_post_small_video(self):
    #     msg = self.main.post_small_video()
    #     assert "话题发表中" in msg