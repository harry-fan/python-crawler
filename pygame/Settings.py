<<<<<<< HEAD
class Settings(object):
    def __init__(self):
        '''背景平台'''
        self.screen_width = 800
        self.screen_height = 900
        self.bg_color = (230,230,230)
        '''ship setting'''
        # self.ship_speed = 1.5
        self.ship_limit = 3
        '''子弹配置'''
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100,0,10)
        #self.bullet_speed = 2
        self.bullets_allowed = 3
        '''monster'''
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.alien_points = 30
        self.fleet_direction   = 1
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

=======
class Settings(object):
    def __init__(self):
        '''背景平台'''
        self.screen_width = 800
        self.screen_height = 900
        self.bg_color = (230,230,230)
        '''ship setting'''
        # self.ship_speed = 1.5
        self.ship_limit = 3
        '''子弹配置'''
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (100,0,10)
        #self.bullet_speed = 2
        self.bullets_allowed = 3
        '''monster'''
        self.fleet_drop_speed = 10

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 2
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        self.alien_points = 30
        self.fleet_direction   = 1
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

>>>>>>> 6a8393942b2abb001636eb387c1d7007844f4613
        self.alien_points = int(self.alien_points * self.score_scale)