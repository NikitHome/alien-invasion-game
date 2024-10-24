import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Класс для управления снарядами, выпущенными кораблем."""
    
    def __init__(self, screen, settings, ship):
        """Создает объект снарядов в текущей позиции корабля."""
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.color = self.settings.bullet_color
        
        # Создание снаряда в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ship.rect.midtop
        
        # Позиция снаряда храниться в вещественном формате.
        self.y = float(self.rect.y)
        
    def update(self):
        """Перемещает снаряд вверх по экрану."""
        
        # Обновление позиции снаряда в вещественном формате.
        self.y -= self.settings.bullet_speed
        # Обновление позиции прямоугольника.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Вывод снаряда на экран."""
        pygame.draw.rect(self.screen, self.color, self.rect)