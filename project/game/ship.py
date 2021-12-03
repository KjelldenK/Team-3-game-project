import arcade

from game.entity import Entity
from game import constants

class Ship(Entity):
    # a sub class of entity that helps make ship type objects
    def __init__(self, texture):
        super().__init__(texture, scale= constants.SHIP_SPRITE_SCALING)

        self._ship_texture = texture
        self._attack_speed = 5
        self._ship_speed = 150
        self._defence = 3
        self.ship_scale = 0.5
        self.shooting = False
        self.right_movment = False
        self.left_movment = False
        self.bullet_list = arcade.SpriteList()

    def get_speed(self):
        # returns the ships speed
        return self._ship_speed

    def get_defence(self):
        # returns the ships defence
        return self._defence

    def get_attack_speed(self):
        # returns the ships attack speed
        return self._attack_speed
    
    def get_texture(self):
        # returns the texture of the ship
        return self._ship_texture

    def action(self, ship_action, status):
        # takes in input from the game and turns it into player actions
        if ship_action == "right":
            self.right_movment = status

        if ship_action == "left":
            self.left_movment = status

        if ship_action == "shoot":
            self.shooting = status
        

    def get_bullet_list(self):
        return self.bullet_list