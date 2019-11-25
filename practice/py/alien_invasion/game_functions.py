import sys
import pygame
from bullet import Bullet
from random import randint
from alien import Alien

def check_kd_events(event, ai_setting, screen, ship, bullets):
    """响应鼠标和键盘事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_setting, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_ku_events(event, ship):
    """响应鼠标和键盘事件"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """响应鼠标和键盘事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_kd_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_ku_events(event, ship)


def update_screen(ai_setting, screen, ship, bullets, aliens):
    """更新屏幕上的图像，并更新到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_setting.screen_bg_color)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

def update_bullets(bullets):
    """更新子弹的位置，删除已经消失的子弹"""
    # 更新子弹的位置
    bullets.update()

    # 删除已消失的子弹
    for bullet in bullets.sprites():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

def update_aliens(aliens, ai_setting):
    """更新外星人的位置，删除已经消失的外星人"""
    # 更新子弹的位置
    aliens.update()

    # 已消失的外星人向相反方向移动
    # for alien in aliens.sprites():
        # if alien.rect.x >= ai_setting.screen_width:
            # aliens.update_left(alien)


def fire_bullet(ai_settings, screen, ship, bullets):
    # 创建一颗子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullet_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - (ai_settings.alien_width * 2)
    number_aliens_x = int(available_space_x/(alien_width * 2))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - (ai_settings.alien_height * 3) - ship_height
    number_rows = int(available_space_y/(alien_height * 2))
    return number_rows

def create_alien(ai_settings, screen, aliens, row_num, alien_number ):
    # 创建一个外星人并将其加入到当前行
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.rect.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_num
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship, aliens):
    alien = Alien(ai_settings, screen)
    alien_number = get_number_aliens_x(ai_settings, alien.rect.width)
    alien_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # 创建第一行外星人
    for row_num in range(alien_rows):
        for alien_number in range(alien_number + 1):
            create_alien(ai_settings, screen, aliens, row_num, alien_number)
