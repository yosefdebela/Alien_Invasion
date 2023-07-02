import pygame
from pygame.sprite import Sprite
class Ship():
    def __init__(self, ai_settings, screen):
        """initializing the shop and its position"""
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/rocket.bmp')
        self.rect = self.image.get_rect()
        # 3
        self.screen_rect = screen.get_rect()
        # starting position
        # 4
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
    #     moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update position based on movement"""
        # update ship center value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
    #  update rect object from self.center
        self.rect.centerx = self.center


    def blitme(self):
        """drow ship at its current locatin"""
        self.screen.blit(self.image, self.rect)
