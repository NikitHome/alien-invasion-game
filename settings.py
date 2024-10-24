class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    
    def __init__(self):
        """Инициализирует настройки игры."""
        
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        # Назначение цвета фона.
        self.bg_color = (210, 210, 210)
        
        # Настройки корабля.
        self.ship_limit = 3
        self.ship_speed = 2

        # Параметры снаряда.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1000
        
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        
        # Темп ускорения игры.
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельца.
        self.score_scale = 1.5
                
        # Настройки пришельцев.
        self.alien_speed = 1.0
        # Подсчет очков.
        self.alien_points = 50
        
    def increase_speed(self):
        """Увеличивает настройки скорости и стоимости пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)