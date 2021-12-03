import arcade
from game import constants

class Entity(arcade.Sprite):
    def __init__(self, texture, scale):
        super().__init__()
        self.scale = scale
        self.Entity_texture = arcade.load_texture(texture)
        self.texture = self.Entity_texture
        self.set_hit_box(self.Entity_texture.hit_box_points)
        self._hit_box_algorithm = 'Detailed'