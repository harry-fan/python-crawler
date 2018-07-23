
class GameStats():
    def __init__(self, ai_settings):
        self.ai_sttings = ai_settings
        self.reset_stats()
        '''开始游戏状态'''
        self.game_active = False
        self.high_score = 0
    def reset_stats(self):
        self.ships_left = self.ai_sttings.ship_limit
        self.score = 0
        self.level = 1
