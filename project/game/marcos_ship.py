import arcade
from arcade.sound import load_sound
from game import constants
from game.ship import Ship

class Marcos_Ship(Ship):
    # this is the testing player ship this is one of many ships the will be in the game
    def __init__(self):
        super().__init__("project\images\Player ships\playerShip1_blue.png")
        
        self._ship_name = "The gunner"
        self._ships_special = "Shoots slow but shoots 3 shots"
        self.time_since_last_firing = 1.0 
        self._attack_speed = 0.8
        self._ship_speed = 350
        self._defence = 4
        self.laser_sound = load_sound("project\sounds\sfx_laser1.ogg")
        

        
    def on_update(self, delta_time: 1 / 60):
        # Update this sprite. 
        if self.left < 0:
            self.left = 1

        if self.right > constants.SCREEN_WIDTH:
            self.right = constants.SCREEN_WIDTH - 1

        if self.right_movment == True:
            self.center_x += self._ship_speed * delta_time

        if self.left_movment == True:
            self.center_x -= self._ship_speed * delta_time

        self.time_since_last_firing += 1 * delta_time


        # makes this ship shoot 3 shots 
        if self.shooting == True:
            if self.time_since_last_firing > self._attack_speed:
                self.bullet = arcade.Sprite("project\images\Lasers\laserBlue01.png", scale= 0.5)
                self.bullet.center_x = self.center_x
                self.bullet.bottom = self.top
                self.bullet.change_y = 20
                self.bullet_list.append(self.bullet)
                self.time_since_last_firing = 0

                self.bullet = arcade.Sprite("project\images\Lasers\laserBlue01.png", scale= 0.5)
                self.bullet.center_x = self.center_x
                self.bullet.bottom = self.top
                self.bullet.change_y = 20
                self.bullet.change_x = 5
                self.bullet.angle = -5
                self.bullet_list.append(self.bullet)
                self.time_since_last_firing = 0

                self.bullet = arcade.Sprite("project\images\Lasers\laserBlue01.png", scale= 0.5)
                self.bullet.center_x = self.center_x
                self.bullet.bottom = self.top
                self.bullet.change_y = 20
                self.bullet.change_x = -5
                self.bullet.angle = 5
                self.bullet_list.append(self.bullet)
                arcade.play_sound(self.laser_sound)
                self.time_since_last_firing = 0