import arcade
from game.entity import Entity

class Tesing_Alien(Entity):
    # This class make the alien object this is for testing ememy types

    def __init__(self,image_file, scale, alian_bullet_list, time_between_firing):
        super().__init__(image_file, scale)

        self.alian_bullet_list = alian_bullet_list
        self.alian_speed = 20
        self._score = 10
        self.timer = 0
        self.bullet_type = "project\images\enemy ships\laserRed06.png"


    def on_update(self, delta_time):
        # moves the alians side to side and moves them down at the end of each movement
        if self.timer < 4:
            self.center_x += self.alian_speed * delta_time
            self.timer + 1 * delta_time
            self.timer += 1 * delta_time

        else:
            self.center_y -= 50
            self.alian_speed = self.alian_speed * -1
            self.timer = self.timer * -1 
        
        pass
            

    def get_value(self):
        return self._score


    