import sys
import pygame
from bullet import Bullet



def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """reslpond to keypress"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        if len(bullets) < ai_settings.bullets_allowed:

        #creating a new bullet to fire
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)
def check_keyup_events(event, ship):
    """respond to key release"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """keyboard and mouse motion"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def update_screen(ai_settings, screen, ship, bullets):
    """update image on screen and flip tonew screen"""
    #redraw all bullets behind the ship
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()