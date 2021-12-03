import arcade
from game.entity import Entity

class Tesing_Alien(Entity):
    # This class make the alien object this is for testing ememy types

    def __init__(self,image_file, scale, alian_bullet_list, time_between_firing):
        super().__init__(image_file, scale)

        self.alian_bullet_list = alian_bullet_list
        self.alian_speed = 100
        self.shooting = False
        self._score = 10

    def on_update(self, delta_time):
        pass
            

    def get_value(self):
        return self._score


    