import sys
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """reslpond to keypress"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
        """fire bullet if no limit is reached"""        
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

def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update image on screen and flip tonew screen"""
    #redraw all bullets behind the ship
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)
    # alien.blitme()
    pygame.display.flip()

def update_bullets(bullets):
    """update bullet position and get rid of the old ones"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
                bullets.remove(bullet)

def create_fleet(ai_settings, screen, aliens):
    """create full of fleets"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    available_space_x = ai_settings.screen_width - 2* alien_width
    number_aliens_x = int(available_space_x / ( 2* alien_width))
    #create first row of aliens

    for alien_number in range(number_aliens_x):
        alien = Alien(ai_settings, screen)
        alien.x = alien_width + 2 * alien_width *alien_number
        alien.rect.x = alien.x