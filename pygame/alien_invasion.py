<<<<<<< HEAD
'''子弹射击'''
import pygame
from pygame.sprite import Group
from Settings import Settings
from ship import Ship
import check as ck
from button import Button
from gameStats import GameStats
from ScoreBoard import Scoreboard

def run_game():
    '''背景 平台初始化'''
    pygame.init()
    ai_settings = Settings()
    #screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("game play")
    '''开始按钮'''
    play_button = Button(ai_settings, screen, "play")

    '''存储游戏的计分板'''
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    '''游戏背景颜色'''
    bg_color = (230, 230, 230)
    '''创建飞船子弹怪物'''
    ship = Ship(ai_settings, screen)
    # monster = Alien(ai_settings, screen)
    # bullets = Bullet(ai_settings, screen, ship)
    # bullets = pygame.sprite.Group()
    bullets = Group()
    #aliens = pygame.sprite.Group()
    aliens = Group()
    '''创造舰队'''
    ck.create_fleet(ai_settings, screen, ship, aliens)

    #game_loop
    while True:
        ck.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            ck.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            ck.update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()
        ck.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()
=======
'''子弹射击'''
import pygame
from pygame.sprite import Group
from Settings import Settings
from ship import Ship
import check as ck
from button import Button
from gameStats import GameStats
from ScoreBoard import Scoreboard

def run_game():
    '''背景 平台初始化'''
    pygame.init()
    ai_settings = Settings()
    #screen = pygame.display.set_mode((1200,800))
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("game play")
    '''开始按钮'''
    play_button = Button(ai_settings, screen, "play")

    '''存储游戏的计分板'''
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    '''游戏背景颜色'''
    bg_color = (230, 230, 230)
    '''创建飞船子弹怪物'''
    ship = Ship(ai_settings, screen)
    # monster = Alien(ai_settings, screen)
    # bullets = Bullet(ai_settings, screen, ship)
    # bullets = pygame.sprite.Group()
    bullets = Group()
    #aliens = pygame.sprite.Group()
    aliens = Group()
    '''创造舰队'''
    ck.create_fleet(ai_settings, screen, ship, aliens)

    #game_loop
    while True:
        ck.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            ck.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            ck.update_aliens(ai_settings,screen, stats, sb, ship, aliens, bullets)
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()
        ck.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)
run_game()
>>>>>>> 6a8393942b2abb001636eb387c1d7007844f4613
