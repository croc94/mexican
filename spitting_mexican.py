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

#Инициализируем настройки игры
game_settings = settings.GameSettings ()

#Создание группы для хранения пуль
bullets = Group () 

#Инициализируе рабочие методы игры
func = functionality.WorkingClass (game_settings, bullets,)



while True:
    #Основной циклы игры
    #Проверяем события возникающие в игре
    func.check_events ()
    
    #Закрашиваем фон игры
    game_settings.screen.fill (game_settings.screen_background_color)

    #Двигаем мексиканца
    func.mexican_move_up  ()
    func.mexican_move_down ()

    bullets.update ()

    game_settings.screen.blit (game_settings.mexican_image, game_settings.mexican_rect,)

    func.update_bullets ()
        
    pygame.display.flip ()