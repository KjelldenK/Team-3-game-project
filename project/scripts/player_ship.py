class Player_Ship:
    """This is the Player_Ship class it will be the parent class for all the types of ships
    The game will let the player play as.
    """
    def __init__(self):
        self.sprit = ""
        self.ship_speed = 100
        self.ship_attack_speed = 10
        self.ship_x = 400
        self.ship_y = 100

    
    def get_sprit(self):
        """Gets the sprit for the given ship"""
        return self.sprit

    def get_ship_speed(self):
        """gets the speed for the given ship"""
        return self.ship_speed

    def get_ship_attack_speed(self):
        """gets the attack speed of the given ship aka how often the ship will shoot"""
        return self.ship_attack_speed

    def get_ship_x(self):
        """gets the starting x position of the ship"""
        return self.ship_x

    def get_ship_y(self):
        """gets the starting y position of the ship"""

        return self.ship_y








