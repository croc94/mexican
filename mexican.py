'''Модуль для хранения кода мексиканца'''

import pygame

class Mexican ():
    '''Модуль для представления мексинаца'''
    def __init__(self, game_settings) -> None:
        #Параметры  изображения мексиканца
        self.mexican_image = pygame.image.load ('images/mexican.bmp')
        self.mexican_rect = self.mexican_image.get_rect ()
        self.game_settings = game_settings
        self.mexican_rect.centery = self.game_settings.screen_center_y

        #Флаг для непрерывного движения мексиканца
        self.move_up_flag = True
        self.move_down_flag = True
        
        #Скорость перемещения мексиканца и снаряда
        self.speed_factor = 1
        self.fire_factor = 0.1

    def mexican_move_up (self):
        #Мексиканец двигается вверх
        if self.move_up_flag == False and self.mexican_rect.top > 0:
            self.mexican_rect.top -= self.speed_factor

    def mexican_move_down (self):
        #Мексиканец двигается вверх
        if self.move_down_flag == False and self.mexican_rect.bottom < self.game_settings.screen_height:
            self.mexican_rect.bottom += self.speed_factor

    def move (self):
        self.mexican_move_up ()
        self.mexican_move_down ()
        self.blit_me ()

    def blit_me (self):
        self.game_settings.screen.blit (self.mexican_image, self.mexican_rect,)