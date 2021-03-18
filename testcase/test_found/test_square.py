from autotest_price.price_android.price_page.app import App


class TestSquare:
    def setup_class(self):
        self.app = App()
        self.main = self.app.start().found().goto_square()

    def setup(self):
        pass

    def teardown_class(self):
        self.app.base_quit()

    def teardown(self):
        pass

    # 搜索帖子或用户
    def test_search(self):
        user, name = self.main.search()
        assert user == name

    # 热门话题-精选tab-点赞
    def test_selected_topic_like(self):
        count, count_liked = self.main.selected_topic_like()
        assert abs(count_liked-count) == 1

    # 热门话题-精选tab-评论
    def test_selected_topic_comment(self):
        msg = self.main.selected_topic_comment()
        assert msg == "评论成功，已进入审核"

    # 热门话题-精选tab-话题详情
    def test_selected_topic_detail(self):
        name, user = self.main.selected_topic_detail()
        assert name == user

    # 热门话题-精选tab-图文话题详情-进入发布者详情页-关注
    def test_selected_topic_detail_author_focus(self):
        focus = self.main.selected_topic_detail_author_focus()
        assert focus == "已关注"

    # 热门话题-精选tab-图文话题详情-进入发布者详情页-粉丝
    def test_selected_topic_detail_author_fans(self):
        username = self.main.selected_topic_detail_author_fans()
        assert username == "大全儿6359微博"

    # 热门话题-精选tab-进入图文话题详情-分享-消息
    def test_selected_topic_detail_share_news(self):
        msg_title = self.main.selected_topic_detail_share_news()
        assert msg_title == "社区消息 "

    # 热门话题-精选tab-进入图文话题详情-评论
    def test_selected_topic_detail_comment(self):
        msg = self.main.selected_topic_detail_comment()
        assert msg == "评论成功，已进入审核"

    # 热门话题-精选tab-进入图文话题详情-收藏
    def test_selected_topic_detail_collection(self):
        msg = self.main.selected_topic_detail_collection()
        assert msg == "话题收藏成功"

    # 热门话题-最新tab-进入小视频话题详情
    # def test_selected_newest_detail(self):
    #     username, name = self.main.selected_newest_detail()
    #     assert username in name

    # 车型社区列表-选择车型-关注
    def test_car_community_select_car_focus(self):
        focus = self.main.car_community_select_car_focus()
        assert focus == "已关注"

    # 固定车型社区-精华tab
    def test_essence(self):
        author, username = self.main.essence()
        assert author == username

    # 固定车型社区-最新tab
    def test_newest(self):
        author, username = self.main.newest()
        assert author == username

    # 固定车型社区-经销商tab-经销商详情
    def test_dealers_detail(self):
        dealer_name, dealer_name_detail = self.main.dealers_detail()
        assert dealer_name_detail == dealer_name

    # 固定车型社区-经销商tab-贷款
    def test_dealers_loan(self):
        submit = self.main.dealers_loan()
        assert submit == "申请贷款"

    # 固定车型社区-经销商tab-询底价
    def test_dealers_ask_price(self):
        btn = self.main.dealers_ask_price()
        assert btn == "获取底价"

    # 车型社区列表页-点击第一条数据
    def test_car_community_list(self):
        topic_user, user = self.main.car_community_list()
        assert topic_user == user

    # 每日榜单—热门帖子-图文帖子详情
    def test_daily_list_hot_topic_detail(self):
        topic_user, user = self.main.daily_list_hot_topic_detail()
        assert topic_user == user

    # 每日榜单—热门帖子-小视频帖子详情
    def test_daily_list_hot_video_detail(self):
        title, title_detail = self.main.daily_list_hot_video_detail()
        assert title == title_detail

    # 每日榜单—评论最多-帖子详情
    def test_daily_list_most_comments_detail(self):
        count, count_detail = self.main.daily_list_most_comments_detail()
        assert count == count_detail

    # 每日榜单—获赞最多-帖子详情
    def test_daily_list_most_likes_detail(self):
        topic_user, user = self.main.daily_list_most_likes_detail()
        assert topic_user == user

    # 提车
    def test_pick_up_the_car(self):
        title = self.main.pick_up_the_car()
        assert title == "提 车"

    # 活动
    def test_activity(self):
        title = self.main.activity()
        assert title == "活 动"

    # 选车
    def test_select(self):
        title = self.main.select()
        assert title == "选 车"

    # 用车
    def test_use_car(self):
        title = self.main.use_car()
        assert title == "用 车"

    # 视频
    def test_video(self):
        title = self.main.video()
        assert title == "视 频"

    # 游记
    def test_travel(self):
        title = self.main.travel()
        assert title == "游 记"

    # 问答
    def test_qa(self):
        title = self.main.qa()
        assert title == "问 答"

    # 新鲜事
    def test_something_new(self):
        title = self.main.something_new()
        assert title == "新 鲜 事"

    # 点击广场中的图文帖子
    def test_square_topic_detail(self):
        topic_user, user = self.main.square_topic_detail()
        assert topic_user == user

    # 发布小视频
    def test_post_video(self):
        msg = self.main.post_video()
        assert "话题发表中" in msg





