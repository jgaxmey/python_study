import pygame
class Ship:
    '''飞船'''
    def __init__(self,ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        # 在飞船的属性x中存储小数值
        self.x = float(self.rect.x)
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        '''根据移动标志调整飞船的位置'''
        # 更新飞船而不是rect对象的x值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # 根据self.x更新rect对象
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)