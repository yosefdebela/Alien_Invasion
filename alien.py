import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """single alien fleet """
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        """load alien image"""
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #storing alien position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw alien at a positin"""
        self.screen.blit(self.image, self.rect)