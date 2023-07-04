# import sys
import pygame
from pygame.sprite import Group
from setting import Settings
from ship import Ship
from alien import Alien

import game_functions as gf


def run_game():
    # initializing pygame
    pygame.init()
    ai_settings = Settings()
    # this make ai_setting an instance of setting class

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # make a ship
    ship = Ship(ai_settings, screen)
    # make a group to store bullet in
    bullets = Group()  
    alien = Alien(ai_settings, screen)
    aliens = Group()
    # create a fleet of aleins
    gf.create_fleet(ai_settings, screen, aliens)


    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        #print(len(bullets))
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)

        """this function will continually update the screen display"""
run_game()
#coment added