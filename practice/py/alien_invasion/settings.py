class Settings():
    """存储外星人入侵的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 500
        #self.bg_color = (230, 230, 230)
        self.screen_bg_color = (255, 255, 255)

        # 飞船设置
        self.ship_speed_factor = 1.5

        # 子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = 100, 0, 0
        self.bullet_allowed = 4

        # 外星人设置
        self.alien_width = 32
        self.alien_height = 32
