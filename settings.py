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

        
        #Параметры  изображения мексиканца
        self.mexican_image = pygame.image.load ('images/mexican.bmp')
        self.mexican_rect = self.mexican_image.get_rect ()
        self.mexican_rect.centery = self.screen_center_y

        #Флаг для непрерывного движения мексиканца
        self.move_up_flag = True
        self.move_down_flag = True


        #Скорость перемещения мексиканца и снаряда
        self.speed_factor = 1
        self.fire_factor = 0.1

        #Параметры снарядов(текста), выпускаемых мескиканцем
        self.fontObj = pygame.font.Font(None, 24)
        self.text = self.fontObj.render('PIY-PIY', True, (0, 0, 0))
        self.text_rect = self.text.get_rect ()
        self.text_rect.right = self.mexican_rect.right
        #self.text_flag = True

        #Параметры для группы пуль

