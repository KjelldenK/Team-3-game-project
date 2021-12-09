import arcade
import game.menu
from game import constants
import game.menu
class Score_screen(arcade.View):
    # this class will display the score after the player dies
    def __init__(self, score):
        super().__init__()
        self.score = score
        self.menu_Background = "project\images\Backgrounds\darkPurple.png"


    def on_draw(self):
        #draws the score on the screen so they player can know how well they did
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, arcade.load_texture(self.menu_Background))
        arcade.draw_text(f"Your final score: {self.score}",constants.SCREEN_WIDTH / 2 , constants.SCREEN_HEIGHT / 2, arcade.color.BLACK, font_size=15,anchor_x="center", font_name = "Kenney Rocket")
        arcade.draw_text(f"Press space to return to menu",constants.SCREEN_WIDTH / 2 , constants.SCREEN_HEIGHT / 2 - 75, arcade.color.BLACK, font_size=15,anchor_x="center", font_name = "Kenney Rocket")


    def on_key_press(self, key, modifiers):
        # When the player hits space it will send them back to the menu screen
        if key == arcade.key.SPACE:
            menu = game.menu.MenuView()
            self.window.show_view(menu)
