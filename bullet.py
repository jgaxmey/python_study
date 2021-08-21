import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''管理子弹'''
    def __init__(self,ai_game):
        '''在飞船位置创建一个子弹'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        #在0，0处创建一个子弹
        self.rect = pygame.Rect(0,0,self.settings.buller_width,self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)

    def update(self):
        '''向上移动子弹'''
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y
    def draw_bullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
        