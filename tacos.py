'''Модуль для хранения кода пришельцев'''

import pygame
from pygame.sprite import Sprite

class Tacos(Sprite):
    '''Класс представляющий однин такос'''
    def __init__(self, settings, ) -> None:
        '''Инициализирует пришельца и задает начальную позицию'''
        super().__init__()
        self.settings = settings

        #Загрузка изображения тако и назначение аттрибута rect
        self.image = pygame.image.load ('images/tacos.bmp')
        self.rect = self.image.get_rect ()

        #Доработка для изменения размера изображения корабля
        scale = 0.05
        self.image = pygame.transform.scale (self.image, (self.rect.width * scale, self.rect.height * scale))
        self.rect = self.image.get_rect ()

        #Каждый новый пришелец появляется в левом верхнем углу экрана
        self.rect.right = self.settings.screen_width - 2 * self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной позиции тако
        self.y = float (self.rect.y)
    
    def blitme (self):
        '''Выводит тако в текущем положении'''
        self.settings.screen.blit (self.image, self.rect)