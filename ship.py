import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Класс для управления кораблем."""
    
    def __init__(self, screen, settings):
        """Инициализирует корабль и задает его начальную позицию."""
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.settings = settings
        
        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('assets/space_ship/SpaceShip1.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom
                
        # Флаги перемещения.
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Обновляет позицию корабля с учетом флагов."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
                    
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """Размещает корабль в центре нижней стороны."""
        self.rect.midbottom = self.screen_rect.midbottom
        # Сохранение вещественной координаты центра корабля.
        self.x = float(self.rect.x)