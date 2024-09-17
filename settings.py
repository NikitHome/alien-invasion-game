class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (210, 210, 210)
        
        self.ship_limit = 3
        self.ship_speed = 2

        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 1000
        
        self.fleet_drop_speed = 5
        self.fleet_direction = 1
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5
                
        self.alien_speed = 1.0
        self.alien_points = 50
        
    def increase_speed(self):
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)