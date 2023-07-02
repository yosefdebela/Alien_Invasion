# import sys
import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship

import game_functions as gf


def run_game():
    # initializing pygame
    pygame.init()
    ai_settings = Settings()
    # this make ai_setting an instance of setting class

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.scree_height))
    pygame.display.set_caption("Alien Invasion")
    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullet in
    bullets = Group()  

    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
        # ship.blitme()
        # pygame.display.flip()
        """this function will continually update the screen display"""
run_game()
#coment added