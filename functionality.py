'''Модуль для описания методов обеспечивающих работу игры'''

import pygame
import sys
from bullet import Bullet

class WorkingClass ():
    #Класс для описания методов работы игры
    def __init__(self, game_settings, bullets, mexican) -> None:
        self.game_settings = game_settings
        self.bullets = bullets
        self.mexican = mexican

    def fire_bullet (self):
        #Создание новой пули и включение ее в группу
        if len (self.bullets) < self.game_settings.bullets_allowed:
            new_bullet = Bullet (self.game_settings, self.mexican)
            self.bullets.add (new_bullet)
        

    def check_events (self):
        #Перебирает события и вызвает соответствующие методы
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                sys.exit ()
            elif event.type == pygame.KEYDOWN:
                #Поведение для нажатия кнопки
                if event.key == pygame.K_w:
                    #Условие движения вверх
                    if self.mexican.move_up_flag == True:
                        self.mexican.move_up_flag = False
                elif event.key == pygame.K_s:
                    #Условие движения вниз
                    if self.mexican.move_down_flag == True:
                        self.mexican.move_down_flag = False
                elif event.key == pygame.K_SPACE:
                    self.fire_bullet ()

            elif event.type == pygame.KEYUP:
                #Поведение для отпускания кнопки
                if event.key == pygame.K_w:
                    if self.mexican.move_up_flag == False:
                        self.mexican.move_up_flag = True
                elif event.key == pygame.K_s:
                    if self.mexican.move_down_flag == False:
                        self.mexican.move_down_flag = True

    def update_bullets (self):
        #Отображение пуль на экран
        for bullet in self.bullets.sprites ():
            bullet.draw_bullet ()

        #Удаление пуль вышедших за край экрана
        for bullet in self.bullets.copy ():
            if bullet.rect.right >= self.game_settings.screen_width:
                self.bullets.remove (bullet)