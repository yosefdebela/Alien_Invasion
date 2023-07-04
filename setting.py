class Settings():
    """store all settings of alien invasion game   """
    def __init__(self):
        """initialize game setting"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 20, 210)
        self.ship_speed_factor = 1.5
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
