import arcade
import random
from  ship_live import ShipSprite 


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Enemies"
ENEMY_SPEED = 2
ENEMY_VERTICAL_MARGIN = 15
RIGHT_ENEMY_BORDER = SCREEN_WIDTH - ENEMY_VERTICAL_MARGIN
LEFT_ENEMY_BORDER = ENEMY_VERTICAL_MARGIN
ENEMY_MOVE_DOWN_AMOUNT = 30 
SCALE = 0.75


class Enemies(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.BLACK_OLIVE)

        self.frame_count = 0
        # self.player_list = []
        self.enemy_list = []
        self.bullet_list = []
        
         # Enemy movement
        self.enemy_change_x = -ENEMY_SPEED

        # Textures for the enemy
        self.enemy_textures = None

         # Set up Player Lives 
        self.player_sprite = None
        self.lives = 3
        

    def setup(self):
        """ Setup the variables for the game. """
        # self.player_list = arcade.SpriteList()
        self.player_sprite_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()
        self.show_lives = arcade.SpriteList()
        self.ship_life_list = arcade.SpriteList()

        self.player_sprite = ShipSprite(":resources:images/space_shooter/"
                                        "playerShip1_orange.png",
                                        SCALE)
        self.player_sprite_list.append(self.player_sprite)
        self.lives = 4

        # Set up the little icons that represent the player lives.
        cur_pos = 10
        for i in range(self.lives):
            life = arcade.Sprite(":resources:images/space_shooter/"
                                 "playerLife1_blue.png",
                                 SCALE)
            life.center_x = cur_pos + life.width
            life.center_y = life.height
            cur_pos += life.width
            self.ship_life_list.append(life)


# Load the textures for the enemies, one facing left, one right  :resources:images/space_shooter/playerShip1_orange.png", 0.5
        self.enemy_textures = []
        texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_blue.png", mirrored=True)
        self.enemy_textures.append(texture)
        texture = arcade.load_texture(":resources:images/space_shooter/playerShip1_orange.png", mirrored=True)
        self.enemy_textures.append(texture)
       
        # Add top-left enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", 0.5)
        enemy.left  = 0
        enemy.center_x = 120
        enemy.center_y = SCREEN_HEIGHT - enemy.height
        enemy.angle = 180

        self.enemy_list.append(enemy)

 
        # Add top-right enemy ship
        enemy = arcade.Sprite(":resources:images/space_shooter/playerShip1_blue.png", 0.5)
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
        #lives
        self.show_lives.draw()
        self.ship_life_list.draw()

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
        for enemy in self.enemy_list:
            enemy.center_x += self.enemy_change_x

             
        # Check every enemy to see if any hit the edge. If so, reverse the
        # direction and flag to move down.
        move_down = False
        for enemy in self.enemy_list:
            if enemy.right > RIGHT_ENEMY_BORDER and self.enemy_change_x > 0:
                self.enemy_change_x *= -1
                move_down = True
            if enemy.left < LEFT_ENEMY_BORDER and self.enemy_change_x < 0:
                self.enemy_change_x *= -1
                move_down = True

        # Did we hit the edge above, and need to move t he enemy down?
        if move_down:
            # Yes
            for enemy in self.enemy_list:
                # Move enemy down
                enemy.center_y -= ENEMY_MOVE_DOWN_AMOUNT
                # Flip texture on enemy so it faces the other way
                if self.enemy_change_x > 0:
                    enemy.texture = self.enemy_textures[0]
                # else:
                #     enemy.texture = self.enemy_textures[1]      

              


def main():
    """ Main function """
    window = Enemies(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()







