import pygame

class Ship():
    def __init__(self, screen, settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        
        self.settings = settings
        
        self.image = pygame.image.load('assets/space_ship/SpaceShip1.bmp')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
                
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed
                    
    def blitme(self):
        self.screen.blit(self.image, self.rect)