import arcade
import random


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Enemies"


class Enemies(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        self.frame_count = 0
        # self.player_list = []
        self.enemy_list = []
        self.bullet_list = []
        

    def setup(self):
        """ Setup the variables for the game. """
        # self.player_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        

       
        # Add top-left enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", 0.5)
        enemy.left  = 0
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180

        self.enemy_list.append(enemy)

 
        # Add top-right enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_orange.png", 0.5)
        enemy.right = 0.3
        enemy.center_x = SCREEN_WIDTH - 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180

        self.enemy_list.append(enemy)

             
    def on_draw(self):
        """Render the screen. """

        arcade.start_render()

        self.enemy_list.draw()
        self.bullet_list.draw()

    def on_update(self, time):
        """All the logic to move, and the game logic goes here. """

        # Loop through each enemy that we have
        for enemy in self.enemy_list:
            # Have a random 1 in 200 change of shooting each 1/100th of a second
            odds = 200
            # Adjust odds based on delta-time
            adj_odds = int(odds * (1 / 100) / time)

            if random.randrange(adj_odds) == 0:
                bullet = arcade.Sprite(":resources:images/space_shooter/laserBlue01.png")
                bullet.center_x = enemy.center_x
                bullet.angle = -90
                bullet.top = enemy.bottom
                bullet.change_y = -2
                self.bullet_list.append(bullet)

        # Get rid of the bullet when it flies off-screen
        for bullet in self.bullet_list:
            if bullet.top < 0:
                bullet.remove_from_sprite_lists()

        self.bullet_list.update()

        #set move
        if random.random() < 0.9:
            enemy.left = SCREEN_HEIGHT - enemy.height
            for enemy in self.enemy_list:
                enemy.center_x -= 1 # set the velocity
                if enemy.center_x <= 775:
                    for enemy in self.enemy_list:
                        enemy.center_x += 1
                        

def main():
    """ Main function """
    window = Enemies(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

