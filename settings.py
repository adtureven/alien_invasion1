class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (20, 5, 20)
        # 飞船的设置
        self.ship_speed_factor = 1
        self.ship_limit = 3
        # 子弹的设置
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 255, 60
        self.bullets_allowed = 3
        # 外星人设置
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 10
        self.fleet_direction = 1



