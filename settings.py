'''Модуль для хранения настроек игры'''

import pygame

class GameSettings ():
    '''Настройки игры'''
    def __init__(self) -> None:
        #Настройки экрана
        self.screen_width = 720
        self.screen_height = 640
        self.screen = pygame.display.set_mode ((self.screen_width, self.screen_height))
        self.screen_background_color = (255, 153, 51)
        pygame.display.set_caption('Mexican spitting')
        self.mini_image = pygame.image.load('images/logo.bmp')
        pygame.display.set_icon (self.mini_image)
        self.screen_center_y = self.screen.get_rect ().centery

        #Параметры пули
        self.bullet_speed_factor = 1
        self.bullet_width = 20
        self.bullet_height = 5
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3