'''Модуль описывающий снаряд(текст)'''

from pygame.sprite import Sprite

class TextBullet (Sprite):
    '''Класс имитирующий пулю'''
    def __init__(self, game_settings) -> None:
        super().__init__()
        self.game_settings = game_settings

        
        self.text_rect = self.game_settings.text.get_rect ()
        self.text_rect.right = self.game_settings.mexican_rect.right
        self.text_flag = True

    def update (self):
        #Условие выпуска текста(снаряда)
        if self.text_flag == True:
            self.text_flag = False
            self.game_settings.text_rect.centery = self.game_settings.mexican_rect.centery

        #Задает положение текста
        if self.text_flag == False:
            self.game_settings.text_rect.left += self.game_settings.fire_factor
            self.game_settings.screen.blit (self.game_settings.text, self.game_settings.text_rect)