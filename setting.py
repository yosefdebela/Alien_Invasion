class Settings():
    """store all settings of alien invasion game   """
    def __init__(self):
        """initialize game setting"""
        self.screen_width = 800
        self.scree_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.5
        # bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        
