'''Модуль для описания класса Bullet'''

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''Класс для управления пулями, выпущенными кораблем'''
    def __init__(self, game_settings, screen, ship,) -> None:
        super().__init__()
        self.screen = screen

        #Создание пули в позиции (0,0)и назначение правильной позиции
        self.rect = pygame.Rect (0, 0, game_settings.bullet_width, game_settings.bullet_height, )
        self.rect.left = ship.rect.right
        self.rect.top = ship.rect.centery

        #Позиция пули хранится в вещественном формате
        self.x = float (self.rect.x)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor

    def update (self):
        #Перемещает пулю вправо по экрану
        #Обновление позиции пули в вещественном формате
        self.x += self.speed_factor

        #Обновление позиции прямоугольника
        self.rect.x = self.x

    def draw_bullet (self):
        #Вывод пули на экран
        pygame.draw.rect (self.screen, self.color, self.rect)