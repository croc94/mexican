'''Модуль для описания методов обеспечивающих работу игры'''

import pygame
import sys
from bullet import Bullet
from tacos import Tacos

class WorkingClass ():
    #Класс для описания методов работы игры
    def __init__(self, game_settings, bullets, mexican, gr_tacos,) -> None:
        self.game_settings = game_settings
        self.bullets = bullets
        self.mexican = mexican
        self.gr_tacos = gr_tacos

    def fire_bullet (self):
        #Создание новой пули и включение ее в группу
        if len (self.bullets) < self.game_settings.bullets_allowed:
            new_bullet = Bullet (self.game_settings, self.mexican)
            self.bullets.add (new_bullet)
        

    def check_events (self):
        #Перебирает события и вызвает соответствующие методы
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                #закрывает игру при нажатии кнопки креста в правм верхнем углу окна
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
                    #При нажатии пробела выпустить снаряд
                    self.fire_bullet ()
                elif event.key == pygame.K_q:
                    #При нажатии клавиши q закрыть игру
                    sys.exit ()

            elif event.type == pygame.KEYUP:
                #Поведение для отпускания кнопки
                if event.key == pygame.K_w:
                    #Двигает героя вверх
                    if self.mexican.move_up_flag == False:
                        self.mexican.move_up_flag = True
                elif event.key == pygame.K_s:
                    #Двигает героя вниз
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

    def create_army (self):
        #Создает армию такос
        #Создание такос и вычисление количества такос в столбце
        #Интервал между соседними такос равен одной ширине такос
        new_tacos = Tacos (self.game_settings,)
        number_tacos_y = self.get_number_tacos_y ()
        number_columns = self.get_number_columns ()

        #Создание создание флота
        for column_number in range (number_columns):
            for tacos_number in range (number_tacos_y):
                self.create_tacos (tacos_number, column_number,)

    def get_number_tacos_y (self):
        #Вычисляет колличество такос в ряду
        new_tacos = Tacos (self.game_settings,)
        tacos_height = new_tacos.rect.height
        available_space_y = self.game_settings.screen_height - 2 * tacos_height
        number_tacos_y = int (available_space_y / (2 * tacos_height))
        return number_tacos_y
    
    def get_number_columns (self):
        #Определяет колличество столбцов, помещающихся на экране
        new_tacos = Tacos (self.game_settings,)
        tacos_width = new_tacos.rect.width
        available_space_x = (self.game_settings.screen_width - (3 * new_tacos.rect.width) - self.mexican.mexican_rect.width)
        number_columns = int (available_space_x / (2 * tacos_width))
        return number_columns
    
    def create_tacos (self, tacos_number, column_number):
        #Создает пришельца и размещает его в ряду
        new_tacos = Tacos (self.game_settings,)
        tacos_height = new_tacos.rect.height
        new_tacos.y = tacos_height + 2 * tacos_height * tacos_number
        new_tacos.rect.y = new_tacos.y
        new_tacos.x = self.game_settings.screen_width - 2 * new_tacos.rect.width * column_number
        new_tacos.rect.x = new_tacos.x
        self.gr_tacos.add (new_tacos)