'''Основной файл игры плюющегося мексиканца'''

#Импортируем pygame
import pygame
pygame.init ()

#Импортируем модуль с настройками игры
import settings

#ИМпортируем модуль с методами обеспечивающими работу игры
import functionality

#Импортируем класс Group из pygame.sprite
from pygame.sprite import Group

#Импортируем класс Mexican
from mexican import Mexican

#Импортируем класс Tacos
from tacos import Tacos

#Инициализируем настройки игры
game_settings = settings.GameSettings ()

#Создание группы для хранения пуль
bullets = Group () 

#Инициализация изображения мексиканца
mexican = Mexican (game_settings)

#Создание такос
tacos = Tacos (game_settings, )

#Инициализируе рабочие методы игры
func = functionality.WorkingClass (game_settings, bullets, mexican)

while True:
    #Основной циклы игры
    #Проверяем события возникающие в игре
    func.check_events ()
    
    #Закрашиваем фон игры
    game_settings.screen.fill (game_settings.screen_background_color)

    #Двигаем мексиканца и прожигаем(отображаем)
    mexican.move ()

    #game_settings.screen.blit (mexican.mexican_image, mexican.mexican_rect,)

    bullets.update ()

    func.update_bullets ()

    #Прожигаем такос на экране
    tacos.blitme ()
        
    pygame.display.flip ()