
from scripts import constants
import arcade
from scripts.pause import PauseView

class GameView(arcade.View):
    """Game view this is the main view it takes in the player ship that was chosen and you start playing the game"""
    def __init__(self, player):
        super().__init__()
        self.player_ship = player
        self.player_sprite = arcade.Sprite(self.player_ship.get_sprit(), constants.SPRITE_SCALING)
        self.player_sprite.center_x = self.player_ship.get_ship_x()
        self.player_sprite.center_y = self.player_ship.get_ship_y()
         

        self.right = False
        self.left = False
        
        

    def on_show(self):
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """Draws all the sprites on the screen"""
        arcade.start_render()
        # Draw all the sprites.
        self.player_sprite.draw()

        # Show tip to pause screen
        arcade.draw_text("Press Esc. to pause",constants.WIDTH / 2, constants.HEIGHT - 100, arcade.color.BLACK, font_size=20, anchor_x="center")

    def on_update(self, delta_time):
        # Call update on all sprites

        if self.player_sprite.left < 0:
            self.player_sprite.left = 1
        if self.player_sprite.right > constants.WIDTH:
            self.player_sprite.right = constants.WIDTH - 1

        if self.right == True:
            self.player_sprite.center_x += self.player_ship.get_ship_speed() * delta_time


        if self.left == True:
            self.player_sprite.center_x -= self.player_ship.get_ship_speed() * delta_time
            
        self.player_sprite.update()




    def on_key_press(self, key, _modifiers):
        #checks key press so the game know where the player wants to go.
        if key == arcade.key.ESCAPE:
            # pass self, the current view, to preserve this view's state
            pause = PauseView(self, GameView(self.player_ship))
            self.window.show_view(pause)

        if key == arcade.key.LEFT:
            self.left = True

        if key == arcade.key.RIGHT:
            self.right = True



    def on_key_release(self, key, _modifiers):
        # checks to see if a key was released so it can stop moving the player.
        if key == arcade.key.LEFT:
            self.left = False

        if key == arcade.key.RIGHT:
            self.right = False
