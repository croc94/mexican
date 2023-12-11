'''Модуль для описания методов обеспечивающих работу игры'''

import pygame
import sys
from bullet import TextBullet

class WorkingClass ():
    #Класс для описания методов работы игры
    def __init__(self, game_settings, text_bullets) -> None:
        self.game_settings = game_settings
        self.text_bullets = text_bullets

    def mexican_move_up (self):
        #Мексиканец двигается вверх
        if self.game_settings.move_up_flag == False and self.game_settings.mexican_rect.top > 0:
            self.game_settings.mexican_rect.top -= self.game_settings.speed_factor

    def mexican_move_down (self):
        #Мексиканец двигается вверх
        if self.game_settings.move_down_flag == False and self.game_settings.mexican_rect.bottom < self.game_settings.screen_height:
            self.game_settings.mexican_rect.bottom += self.game_settings.speed_factor

    '''def show_text (self):
        #Задает положение текста
        if self.game_settings.text_flag == False:
            self.game_settings.text_rect.left += self.game_settings.fire_factor
            self.game_settings.screen.blit (self.game_settings.text, self.game_settings.text_rect)'''

    def check_events (self):
        #Перебирает события и вызвает соответствующие методы
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                sys.exit ()
            elif event.type == pygame.KEYDOWN:
                #Поведение для нажатия кнопки
                if event.key == pygame.K_w:
                    #Условие движения вверх
                    if self.game_settings.move_up_flag == True:
                        self.game_settings.move_up_flag = False
                elif event.key == pygame.K_s:
                    #Условие движения вниз
                    if self.game_settings.move_down_flag == True:
                        self.game_settings.move_down_flag = False
                elif event.key == pygame.K_SPACE:

                    #Создадим групу пуль
                    new_bullet = TextBullet (self.game_settings)
                    self.text_bullets.add (new_bullet)

                    print (len (self.text_bullets))

                    '''#Условие выпуска текста(снаряда)
                    if self.game_settings.text_flag == True:
                        self.game_settings.text_flag = False
                        self.game_settings.text_rect.centery = self.game_settings.mexican_rect.centery'''

                    

            elif event.type == pygame.KEYUP:
                #Поведение для отпускания кнопки
                if event.key == pygame.K_w:
                    if self.game_settings.move_up_flag == False:
                        self.game_settings.move_up_flag = True
                elif event.key == pygame.K_s:
                    if self.game_settings.move_down_flag == False:
                        self.game_settings.move_down_flag = True
                '''elif event.key == pygame.K_SPACE:
                    #Условие выпуска текста(снаряда)
                    if self.game_settings.text_flag == False:
                        self.game_settings.text_flag = True'''