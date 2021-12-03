import arcade
from arcade.sound import load_sound
from game import constants
from game.ship import Ship

class Player_Test_Ship(Ship):
    # this is the testing player ship this is one of many ships the will be in the game
    def __init__(self):
        super().__init__("project\images\Player ships\playerShip1_red.png")
        
        self.time_since_last_firing = 1.0 
        self._attack_speed = 0.2
        self._ship_speed = 250
        self._defence = 3
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

        if self.shooting == True:
            if self.time_since_last_firing > self._attack_speed:
                self.bullet = arcade.Sprite("project\images\Lasers\laserRed01.png", scale= 0.5)
                self.bullet.center_x = self.center_x
                self.bullet.bottom = self.top
                self.bullet.change_y = 20
                self.bullet_list.append(self.bullet)
                arcade.play_sound(self.laser_sound)
                self.time_since_last_firing = 0


        
