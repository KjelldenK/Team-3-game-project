import arcade
from arcade.text_pyglet import FontNameOrNames
from game.player_text_ship import Player_Test_Ship
from game import constants
from game.gameview import GameView
class Character_Selection_View(arcade.View):
    def __init__(self):
        super().__init__()
        self.menu_Background = "project\images\menu_background.jpg"
        self.ship_number = 0
        self.test_ship = Player_Test_Ship()

    
        self.ship_list = [self.test_ship]
        

    def on_draw(self):
        # draws the character selection screen (changes depending on what ship you are on)
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, arcade.load_texture(self.menu_Background))
        arcade.draw_texture_rectangle(constants.SCREEN_WIDTH // 2, constants.SCREEN_HEIGHT // 2 + 50, 100, 100, arcade.load_texture(self.ship_list[self.ship_number].get_texture()))
        arcade.draw_text(f"attack stat: {self.ship_list[self.ship_number].get_attack_speed()}",constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2 - 30, arcade.color.BLACK, font_size=15, anchor_x="center", font_name = "Kenney Rocket")
        arcade.draw_text(f"speed stat: {self.ship_list[self.ship_number].get_speed()}",constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2 - 60, arcade.color.BLACK, font_size=15, anchor_x="center", font_name = "Kenney Rocket")
        arcade.draw_text(f"speed stat: {self.ship_list[self.ship_number].get_defence()}",constants.SCREEN_WIDTH / 2,constants.SCREEN_HEIGHT / 2 - 90, arcade.color.BLACK, font_size=15, anchor_x="center", font_name = "Kenney Rocket")


    def on_key_press(self, key, _modifiers):
        #checks to see if the player wants to go to the next ship or select the ship.
        if key == arcade.key.RIGHT:
            self.ship_number += 1
            self.ship_number = self.ship_number % len(self.ship_list)
        if key == arcade.key.LEFT:
            self.ship_number -= 1
            self.ship_number = self.ship_number % len(self.ship_list)
        if key == arcade.key.SPACE:
            player = self.ship_list[self.ship_number]
            game = GameView(player)
            self.window.show_view(game)
          